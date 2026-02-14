import pygame
from variables import *

CELL_SIZE = 200
ROWS = 3
COLS = 3

def draw_board(screen, board_img, o_img, x_img):
    screen.blit(board_img, (0, 200))
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE
            y = row * CELL_SIZE + 200
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

            if board[row][col] == -1 :
                img_rect = x_img.get_rect(center=rect.center)
                screen.blit(x_img, img_rect)
            elif board[row][col] == 1 :
                img_rect = o_img.get_rect(center=rect.center)
                screen.blit(o_img, img_rect)
