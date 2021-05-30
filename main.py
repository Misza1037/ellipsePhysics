#main.py
from math import sqrt
import pygame
from pygame.math import Vector2 as V
from time import sleep
pygame.init()

screenSize = (800,600)
screen = pygame.display.set_mode(screenSize)

dx = screenSize[0]//2
dy = screenSize[1]//2
rx = 300
ry = 200


def draw_lines(x, y):
    if y == 0:
        pygame.draw.line(screen, (255, 0, 0), (x+dx, 0), (x+dx, 2*dy))
        return 0
    elif x == 0:
        pygame.draw.line(screen, (255, 0, 0), (dx, 0), (dx, 2*dy))
        return 0

    a = -x * ry**2 / (y * rx**2)
    b = ry**2 / y

    a2 = 0
    if a != 0: a2 = -1/a
    b2 = y - a2 * x

    pygame.draw.line(screen, (255, 0, 0), (0, a*-dx + b+dy), (2*dx, a*dx + b+dy))
    pygame.draw.line(screen, (255, 0, 0), (0, a2*-dx + b2+dy), (2*dx, a2*dx + b2+dy))

    pygame.draw.line(screen, (0, 255, 0), (dx, dy), (dx+x, dy+y))
    VC = V(x, y).reflect(V(1, a2))
    pygame.draw.line(screen, (0, 255, 0), (dx+x, dy+y), (dx+x+VC.x, dy+y+VC.y))


def f(x):
    return ry * sqrt(1 - x**2 / rx**2)


#x = -300
#y = f(x)

for x in range(-300, 301):
    y = f(x)
    screen.fill((255, 255, 255))
    pygame.draw.ellipse(screen, (0, 0, 0), (dx - rx, dy - ry, 2*rx, 2*ry))
    draw_lines(x, y)

    pygame.display.flip()
    sleep(1/120)
for x in range(300, -301, -1):
    y = -f(x)
    screen.fill((255, 255, 255))
    pygame.draw.ellipse(screen, (0, 0, 0), (dx - rx, dy - ry, 2*rx, 2*ry))
    draw_lines(x, y)

    pygame.display.flip()
    sleep(1/120)

sleep(4)
pygame.quit()
