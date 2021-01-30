import pygame

pygame.init()
pygame.mixer.music.load('glamour_tropical.mp3')
pygame.mixer.music.play()
pygame.event.wait()

input('Show!')
