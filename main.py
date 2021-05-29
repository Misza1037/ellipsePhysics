#main.py
import pygame
from time import sleep
pygame.init()
screenSize = [800,600]
screen = pygame.display.set_mode(screenSize)
screen.fill((255, 255, 255))
sx = 100
sy = 100
rx = 600
ry = 400
pygame.draw.ellipse(screen,(0,0,0),(sx, sy, rx, ry))

pygame.display.flip()
sleep(4)
pygame.quit()
