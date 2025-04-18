import pygame
import sys
from level1 import level1
from level2 import level2
from level3 import level3
import psycopg2

def connect_db():
    return psycopg2.connect(
        host="localhost",       
        database="snake_game",  
        user="postgres",        
        password="rollannice336"  
    )

def get_user_data(username):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    
    if user:
        cursor.execute("SELECT level, score FROM user_scores WHERE user_id = %s ORDER BY score_id DESC LIMIT 1", (user[0],))
        user_data = cursor.fetchone()
        if user_data:
            return user[0], user_data[0], user_data[1], 3  # Возвращаем начальные 3 жизни
        else:
            return user[0], 1, 0, 3  # Начальные 3 жизни
    else:
        cursor.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id", (username,))
        user_id = cursor.fetchone()[0]
        conn.commit()
        return user_id, 1, 0, 3  # Начальные 3 жизни

def update_score(user_id, level, score):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT score_id FROM user_scores WHERE user_id = %s AND level = %s", (user_id, level))
    existing_score = cursor.fetchone()
    
    if existing_score:
        cursor.execute("UPDATE user_scores SET score = %s WHERE score_id = %s", (score, existing_score[0]))
    else:
        cursor.execute("INSERT INTO user_scores (user_id, level, score) VALUES (%s, %s, %s)", (user_id, level, score))
    
    conn.commit()
    cursor.close()
    conn.close()

def input_username():
    pygame.init()
    window = pygame.display.set_mode((850, 600))
    pygame.display.set_caption("Введите имя пользователя")
    font = pygame.font.Font(None, 48)
    input_box = pygame.Rect(300, 250, 300, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        
        window.fill((0, 0, 0))
        txt_surface = font.render(text, True, color)
        width = max(300, txt_surface.get_width() + 10)
        input_box.w = width
        window.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(window, color, input_box, 2)
        pygame.display.flip()
        clock.tick(30)

def main():
    username = input_username()  
    user_id, level, score, lives = get_user_data(username)  # Получаем данные игрока, включая количество жизней

    running = True
    while running:
        if level == 1:
            score, lives = level1(score, lives)  # Передаём количество жизней в функцию уровня
            if score >= 5:  # Переход на следующий уровень
                level = 2
                score = 0  # Сбрасываем очки или продолжаем их
        elif level == 2:
            score, lives = level2(score, lives)  # Передаём количество жизней в функцию уровня
            if score >= 5:  # Переход на следующий уровень
                level = 3
                score = 0  # Сбрасываем очки или продолжаем их
        elif level == 3:
            score, lives = level3(score, lives)  # Передаём количество жизней в функцию уровня
            if score >= 5:  # Условие для финального перехода или окончания игры
                running = False

        if lives <= 0:  # Если жизни закончились, игра заканчивается
            running = False

        update_score(user_id, level, score)  # Обновляем уровень и счёт в базе данных
        pygame.time.wait(500)  # Небольшая задержка для смены уровня
    
    pygame.quit()

if __name__ == "__main__":
    main()
