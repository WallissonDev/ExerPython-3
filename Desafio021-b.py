import pygame
pygame.mixer.init()
pygame.mixer.music.load('rihanna.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()