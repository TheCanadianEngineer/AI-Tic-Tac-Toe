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
board_img = pygame.transform.scale(board_img, (600, 600))

bgrd_img = pygame.image.load(r"images\background_tic.png").convert_alpha()
bgrd_img = pygame.transform.scale(bgrd_img, (605, 805))

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

    elapsed_time = pygame.time.get_ticks() - start_time

    screen.fill((0,255,85))

    draw_board(screen, board_img, bgrd_img, o_img, x_img)

    # Timer Rendering TO PUT IN ui.py LATER

    font = pygame.font.Font("fonts/VarelaRound-Regular.ttf", 48)

    text_surface = font.render(format_time(elapsed_time), True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH / 2, 45))
    screen.blit(text_surface, text_rect)

    get_mouse_pos()

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()