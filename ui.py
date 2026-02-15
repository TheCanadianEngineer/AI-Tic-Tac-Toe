import pygame
from variables import *

CELL_SIZE = 200
ROWS = 3
COLS = 3

def draw_board(screen, board_img, bgrd_img, o_img, x_img):
    global elapsed_time, player_wins, ai_wins
    # Main Visuals
    screen.blit(bgrd_img, (-2, -2))
    screen.blit(board_img, (0, 200))

    # Player wins
    font = pygame.font.Font("fonts/VarelaRound-Regular.ttf", 56)

    text_surface = font.render(f'{player_wins}', True, (255, 170, 170))
    text_rect = text_surface.get_rect(center=(90, 135))
    screen.blit(text_surface, text_rect)

    # AI wins
    font = pygame.font.Font("fonts/VarelaRound-Regular.ttf", 56)

    text_surface = font.render(f'{ai_wins}', True, (163, 166, 255))
    text_rect = text_surface.get_rect(center=(513, 135))
    screen.blit(text_surface, text_rect)
    

    # Piece Rendering
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

def format_time(ms):
    global elapsed_time
    seconds = ms // 1000
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"