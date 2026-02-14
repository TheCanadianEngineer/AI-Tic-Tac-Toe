import pygame
from variables import *
import math
from board import *

def get_mouse_pos():
    global mouse_col, mouse_row

    rel_x, rel_y = pygame.mouse.get_pos()

    if rel_y > 200:
        mouse_row = math.floor(rel_x / 200)
        mouse_col = math.floor((rel_y - 200) / 200)

def handle_click():
    global mouse_col, mouse_row, playing

    board_pos = board[mouse_col][mouse_row]

    if board_pos == 0:
        if playing == PLAYER:
            board[mouse_col][mouse_row] = PLAYER
            check_win()
            print(check_draw())
            playing = AI
        elif playing == AI:
            board[mouse_col][mouse_row] = AI
            check_win()
            print(check_draw())
            playing = PLAYER

        