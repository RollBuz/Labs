-- 1. Создание таблицы для телефонной книги
CREATE TABLE phonebook (
    id SERIAL PRIMARY KEY,      
    first_name VARCHAR(100) NOT NULL, 
    phone VARCHAR(15) UNIQUE NOT NULL  
);

-- 2. Вставка данных вручную (одна запись)
INSERT INTO phonebook (first_name, phone)
VALUES 
    ('Роллан', '1234567890'),
    ('Гала', '2345678901'),
    ('Жания', '3456789012');

-- 3. Загрузка данных из CSV файла
-- Этот запрос нужно выполнить в PostgreSQL, убедитесь, что путь к CSV-файлу правильный.
-- Для загрузки используйте команду COPY, которая позволяет загрузить данные из CSV в таблицу.
-- Пример:
-- COPY phonebook (first_name, phone)
-- FROM '/path/to/your/phonebook.csv'
-- DELIMITER ','
-- CSV HEADER;

-- 4. Обновление данных
-- Обновление номера телефона пользователя с именем "Иван"
UPDATE phonebook
SET phone = '9876543210'
WHERE first_name = 'Роллан';

-- 5. Запрос данных
-- Получение всех записей из таблицы
SELECT * FROM phonebook;

-- Получение записи по имени
SELECT * FROM phonebook
WHERE first_name = 'Роллан';

-- 6. Удаление данных
-- Удаление записи по имени
DELETE FROM phonebook
WHERE first_name = 'Роллан';

-- Удаление записи по номеру телефона
DELETE FROM phonebook
WHERE phone = '1234567890';

-- 7. Дополнительные запросы
-- Проверка существования записи по телефону
SELECT * FROM phonebook
WHERE phone = '1234567890';

-- Проверка существования записи по имени
SELECT * FROM phonebook
WHERE first_name = 'Мария';
