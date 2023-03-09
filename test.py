import pygame
from config import *
from prediction import predict

import warnings

# убрать runtime предупреждения
warnings.filterwarnings('ignore')

pygame.init()

width = 45
height = 45
margin = 5

size = (WIDTH * (margin + width) + margin, HEIGHT * (margin + height) + margin)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("neuron")

done = False

clock = pygame.time.Clock()

cells = [0 for _ in range(INP_DIM)]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0] // (width + margin)
            row = pos[1] // (width + margin)
            kek = row*WIDTH+col
            if kek < INP_DIM:
                cells[kek] = int(not cells[kek])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                predict(cells, True)
            if event.key == pygame.K_a:
                print(cells)

    screen.fill("black")

    color = "white"

    for row in range(WIDTH):
        for col in range(HEIGHT):
            if cells[row*HEIGHT+col]:
                color = "cyan"
            pygame.draw.rect(screen, color, [col*width+margin*(col+1), row*height+margin*(row+1), width, height])
            color = "white"

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
