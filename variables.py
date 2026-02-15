import pygame
import numpy as np
# Constants

WHITE = (255, 255, 255)

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

board = np.array([[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]])

mouse_row = 0
mouse_col = 0

playing = PLAYER

player_wins = 2
ai_wins = 13

start_time = 0
elapsed_time = 0

clock = pygame.time.Clock()