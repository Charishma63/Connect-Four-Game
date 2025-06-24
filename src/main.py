from connect_four import *

board = create_board()
print_board(board)

turn = 0
while True:
    col = int(input(f"Player {turn+1} ({'X' if turn == 0 else 'O'}), choose column (0-6): "))
    if 0 <= col < COLS and is_valid_move(board, col):
        row = get_next_row(board, col)
        piece = 'X' if turn == 0 else 'O'
        drop_piece(board, row, col, piece)

        print_board(board)

        if check_win(board, piece):
            print(f"Player {turn+1} wins!")
            break

        turn = (turn + 1) % 2
    else:
        print("Invalid move. Try again.")
