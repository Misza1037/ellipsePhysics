#main.py
w = open("czasy.txt", "w")

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
    a = -x * ry**2 / (y * rx**2)
    print(a)
    b = ry**2 / y + 300
    print(b)
    pygame.draw.line(screen, (0, 0, 0), (0, a*-dx + b), (2*dx, a*dx + b))


def pochodna(x):
    return -x / f(x)


def f(x):
    return ry * sqrt(1 - x**2 / rx**2)


x = 50
y = f(x)

pygame.draw.ellipse(screen, (0, 0, 0), (dx - rx, dy - ry, 2*rx, 2*ry))
draw_line(x, y)
pygame.draw.rect(screen, (255, 0, 0), (dx+x, dy+y, 10, 10))
pygame.display.flip()

for i in range(300):
    w.write(f'{i};{pochodna(i)} \n')

sleep(4)
pygame.quit()
w.close()
