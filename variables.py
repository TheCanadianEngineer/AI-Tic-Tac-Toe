import pygame

# Constants

WIDTH = 600
HEIGHT = 800
ROWS = 3
COLS = 3
SQUARE_SIZE = 200

EMPTY = 0
PLAYER = -1
AI = 1

EMPTY = 0
AI = 1
PLAYER = -1

# Other Variables

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

mouse_row = 0
mouse_col = 0

playing = PLAYER


