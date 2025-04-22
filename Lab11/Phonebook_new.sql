--1
CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(id INT, surname VARCHAR(50), name VARCHAR(50), phone VARCHAR(20)) AS $$
BEGIN
    RETURN QUERY
    SELECT id, surname, name, phone
    FROM phonebook_new
    WHERE surname LIKE '%' || pattern || '%' 
       OR name LIKE '%' || pattern || '%'
       OR phone LIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

select * from search_phonebook('Text') --example

--2
CREATE OR REPLACE PROCEDURE insert_or_update_user(p_surname VARCHAR(50), p_name VARCHAR(50), p_phone VARCHAR(20))
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook_new WHERE surname = p_surname AND name = p_name) THEN
        UPDATE phonebook_new
        SET phone = p_phone
        WHERE surname = p_surname AND name = p_name;
    ELSE
        INSERT INTO phonebook_new (surname, name, phone)
        VALUES (p_surname, p_name, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;

CALL insert_or_update_user('Buzhigitov', 'Ayan', '+7 777 777 7778'); -- example


--3
CREATE OR REPLACE PROCEDURE insert_multiple_users(p_users TEXT[])
AS $$
DECLARE
    p_user TEXT;
    p_surname VARCHAR(50);
    p_name VARCHAR(50);
    p_phone VARCHAR(20);
BEGIN
    FOREACH p_user IN ARRAY p_users LOOP
        p_surname := split_part(p_user, ',', 1);
        p_name := split_part(p_user, ',', 2);
        p_phone := split_part(p_user, ',', 3);
        
        IF p_phone ~ '^\\+7 \\d{3} \\d{3} \\d{4}$' THEN
            INSERT INTO phonebook_new (surname, name, phone)
            VALUES (p_surname, p_name, p_phone);
        ELSE
            RAISE NOTICE 'Incorrect phone number: %', p_phone;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

CALL insert_multiple_users(
    ARRAY[]) --'rollan,trudogolic,+7 777 777 7777', '...'

--4
CREATE OR REPLACE FUNCTION get_phonebook_page(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, surname VARCHAR(50), name VARCHAR(50), phone VARCHAR(20)) AS $$
BEGIN
    RETURN QUERY
    SELECT phonebook_new.id, phonebook_new.surname, phonebook_new.name, phonebook_new.phone
    FROM phonebook_new
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

select * from get_phonebook_page(3,2) --for example
--5

CREATE OR REPLACE PROCEDURE delete_by_something(p_surname VARCHAR(50), p_name VARCHAR(50), p_phone VARCHAR(20))
AS $$
BEGIN
    DELETE FROM phonebook_new
    WHERE surname = p_surname AND name = p_name;

    DELETE FROM phonebook_new
    WHERE phone = p_phone;
END;
$$ LANGUAGE plpgsql;

CALL delete_by_something('Buzhigitov', 'Ayan', NULL);  -- Удалит по имени и фамилии
CALL delete_by_something(NULL, NULL, '+7 777 777 7774');  -- Удалит по телефону