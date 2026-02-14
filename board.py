from variables import *

def check_win():
    size = len(board)

    # Check rows
    for r in range(size):
        if board[r][0] != 0 and all(board[r][c] == board[r][0] for c in range(size)):
            winner = board[r][0]
            break
    else:
        # Check columns
        for c in range(size):
            if board[0][c] != 0 and all(board[r][c] == board[0][c] for r in range(size)):
                winner = board[0][c]
                break
        else:
            # Check main diagonal
            if board[0][0] != 0 and all(board[i][i] == board[0][0] for i in range(size)):
                winner = board[0][0]
            # Check other diagonal
            elif board[0][size-1] != 0 and all(board[i][size-1-i] == board[0][size-1] for i in range(size)):
                winner = board[0][size-1]
            else:
                return 0  # no winner

    if winner == 1:
        print("You lose 😈 (AI wins)")
    elif winner == -1:
        print("You win 🎉")

    return winner

def check_draw():
    for x in range(3):
        for i in range(3):
            if board[x][i] == 0:
                return False
            
    return True