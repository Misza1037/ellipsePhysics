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
r = 300


def draw_line(x, y):
    a = pochodna(x)
    print(a)
    b = dy+(y - a*x)
    print(b)
    pygame.draw.line(screen, (0, 0, 0), (0, a*-dx + b), (2*dx, a*dx + b))


def pochodna(x):
    return -x / f(x)


def f(x):
    return sqrt(r**2 - x**2)


pygame.draw.circle(screen, (0, 0, 0), (dx, dy), r)
draw_line(50, f(50))
pygame.draw.rect(screen, (255, 0, 0), (dx+50, dy+f(50), 10, 10))
pygame.display.flip()

for i in range(300):
    w.write(f'{i};{pochodna(i)} \n')

sleep(4)
pygame.quit()
w.close()
