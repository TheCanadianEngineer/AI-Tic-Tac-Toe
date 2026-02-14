import numpy as np
import pygame
from variables import *
from ui import *
from input_handler import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
clock = pygame.time.Clock()
running = True

board_img = pygame.image.load(r"images\board_tic.png").convert_alpha()

o_img = pygame.image.load(r"images\o_tic.png").convert_alpha()
o_img = pygame.transform.scale(o_img, (160, 160))

x_img = pygame.image.load(r"images\x_tic.png").convert_alpha()
x_img = pygame.transform.scale(x_img, (160, 160))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 1 = left mouse button
                handle_click()

    screen.fill((0,255,85))
    # RENDER YOUR GAME HERE
    draw_board(screen, board_img, o_img, x_img)
    get_mouse_pos()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()