import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((240, 240, 240))
circle(screen, (255, 253, 15), (200, 200), 125) #желтый круг
circle(screen, (0, 0, 0), (200, 200), 125, 3) #черный обод для круга
circle(screen, (255, 0, 0), (250, 180), 20) #красный круг
circle(screen, (255, 0, 0), (150, 180), 30) #красный левый круг
circle(screen, (0, 0, 0), (250, 180),  10) #черный круг
circle(screen, (0, 0, 0), (150, 180), 10)
#Добавляем рот
x1 = 140; y1 = 270
x2 = 260; y2 = 270
N = 10
line(screen, (0, 0, 0), (x1, y1), (x2, y2), 15)
#Добавляем брови
x1 = 120; y1 = 120
x2 = 190; y2 = 170
line(screen, (0, 0, 0), (x1, y1), (x2, y2), 15)
line(screen, (0, 0, 0), (210, 170 ), (280, 120), 15)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()