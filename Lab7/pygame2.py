import pygame
import sys
from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYDOWN, K_p, K_s, K_n, K_b

pygame.mixer.init()
pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Music Player with Buttons")

playlist = [
    "Lab7\\musics\\Redbone - Come and Get Your Love.mp3",
    "Lab7\\musics\\Kendrick Lamar - Money Trees (feat. Jay Rock).mp3",
    "Lab7\\musics\\EI8HT & Offset - Silk and Cologne (Spider-Verse Remix).mp3"
]
images = [
    "Lab7\\images\\image1.jpg",
    "Lab7\\images\\image2.jpg",
    "Lab7\\images\\image3.jpg"
]
buttons = [
    "Lab7\\images\\previous.png",
    "Lab7\\images\\next.png",
    "Lab7\\images\\play.png",
    "Lab7\\images\\stop.png"
]

class MusicPlayer:
    def __init__(self):
        self.current_index = 0
        self.is_playing = True

        self.previous_button = pygame.image.load(buttons[0])
        self.next_button = pygame.image.load(buttons[1])
        self.play_button = pygame.image.load(buttons[2])
        self.stop_button = pygame.image.load(buttons[3])

    def display_photo(self, index):
        screen.fill((255, 255, 255))
        photo = pygame.image.load(images[index])
        photo = pygame.transform.scale(photo, (384, 288))
        x_offset = (400 - 384) // 2
        y_offset = (400 - 384) // 2
        screen.blit(photo, (x_offset, y_offset))
        self.display_buttons()
        pygame.display.flip()

    def display_buttons(self):
        screen.blit(self.previous_button, (50, 325))
        if self.is_playing:
            screen.blit(self.stop_button, (176, 325))
        else:
            screen.blit(self.play_button, (176, 325))
        screen.blit(self.next_button, (302, 325))

    def play_song(self):
        pygame.mixer.music.load(playlist[self.current_index])
        pygame.mixer.music.play()
        self.is_playing = True
        self.display_photo(self.current_index)

    def stop_music(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.display_photo(self.current_index)

    def next_song(self):
        self.stop_music()
        self.current_index = (self.current_index + 1) % len(playlist)
        self.play_song()

    def previous_song(self):
        self.stop_music()
        self.current_index = (self.current_index - 1) % len(playlist)
        self.play_song()

player = MusicPlayer()

player.play_song()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            if 50 <= x <= 98 and 325 <= y <= 373:
                player.previous_song()
            elif 302 <= x <= 350 and 325 <= y <= 373:
                player.next_song()
            elif 176 <= x <= 224 and 325 <= y <= 373:
                if player.is_playing:
                    player.stop_music()
                else:
                    player.play_song()
        elif event.type == KEYDOWN:
            if event.key == K_p:
                player.play_song()
            elif event.key == K_s:
                player.stop_music()
            elif event.key == K_n:
                player.next_song()
            elif event.key == K_b:
                player.previous_song()

    player.display_buttons()
    pygame.display.flip()
