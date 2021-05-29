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


def draw_line(x, y):
    a, b = pochodna(x), sqrt(ry**2 * (1 - (x**2 / rx**2))) - pochodna(x)*x
    pygame.draw.line(screen, (0, 0, 0), (0, a*-dx + b), (2*dx, a*dx + b))


def pochodna(x):
    return -(ry*x)/((rx**2) * (ry*(1-((x**2)/(rx**2))))**0.5)


pygame.draw.ellipse(screen, (0, 0, 0), (dx-rx, dy-ry, 2*rx, 2*ry))
draw_line(100, 100)
pygame.display.flip()

sleep(4)
pygame.quit()
