ROWS = 6
COLS = 7

def create_board():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    for row in board:
        print("|" + "|".join(row) + "|")
    print(" " + " ".join(str(i) for i in range(COLS)))

def is_valid_move(board, col):
    return board[0][col] == " "

def get_next_row(board, col):
    for row in reversed(range(ROWS)):
        if board[row][col] == " ":
            return row

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def check_win(board, piece):
    # Horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col+i] == piece for i in range(4)):
                return True
    # Vertical
    for row in range(ROWS - 3):
        for col in range(COLS):
            if all(board[row+i][col] == piece for i in range(4)):
                return True
    # Diagonal /
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row-i][col+i] == piece for i in range(4)):
                return True
    # Diagonal \
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row+i][col+i] == piece for i in range(4)):
                return True
    return False
