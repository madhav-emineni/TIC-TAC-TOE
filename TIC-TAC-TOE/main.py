import random

board = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]
         ]


def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("- - - - -")


def is_position_valid(position, board):
    position = int(position) - 1
    row = position // 3
    col = position % 3
    return board[row][col] not in ['X', 'O']


def place_marker(marker, position, board):
    position = int(position) - 1
    row = position // 3
    col = position % 3
    board[row][col] = marker


def check_win(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return True


def game():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]
             ]
    choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    current_marker = "X"
    display_board(board)
    while True:

        position = input(f"Player {current_marker}.Enter a number from (1 to 9) to place your marker: ")
        if not position.isdigit() or 0 >= int(position) > 9:
            print("Invalid choice!! Enter a number and in between 0 to 9")
            continue
        if not is_position_valid(position, board):
            print("This place is already occupied please choose any other slot")
            continue
        place_marker(current_marker, position, board)
        display_board(board)
        if check_win(board):
            print(f"Player {current_marker} Wins!!!")
            break
        if all([cell != str(num) for num in range(1, 10) for row in board for cell in row]):
            print("It's a Draw!!!")
            break
        current_marker = "O" if current_marker == 'X' else 'X'


game()
