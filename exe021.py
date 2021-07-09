import pygame

pygame.mixer.init()
pygame.mixer.music.load('GH.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1.0)
while (pygame.mixer.music.get_busy()): pass
