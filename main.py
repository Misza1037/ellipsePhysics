#main.py
from math import sqrt
import pygame
from time import sleep
pygame.init()

screenSize = (800,600)
screen = pygame.display.set_mode(screenSize)
screen.fill((255, 255, 255))

dx = screenSize[0]//2
dy = screenSize[1]//2
rx = 300
ry = 200


def pochodna(x):
    return sqrt(ry**2 * (1 - (x**2 / rx**2)))


pygame.draw.ellipse(screen,(0,0,0),(dx-rx, dy-ry, 2*rx, 2*ry))
pygame.display.flip()

sleep(4)
pygame.quit()
