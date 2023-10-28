board = [[' ' for _ in range(3)] for _ in range(3)]


def check_row(row, player):
    return all(board[row][col] == player for col in range(3))


def check_col(col, player):
    return all(board[row][col] == player for row in range(3))


def check_diagonal(player):
    return (all(board[i][i] == player for i in range(3)) or
            all(board[i][2 - i] == player for i in range(3)))


def print_board():
    print('---------')
    for row in board:
        print('|', end='')
        for cell in row:
            print(cell, end='|')
        print('\n---------')


def play_game():
    turns = 0
    current_player = 'X'

    while turns < 9:
        print_board()
        print(f"Ходит игрок {current_player}.")
        row = int(input("Выберите строку (от 1 до 3): ")) - 1
        col = int(input("Выберите столбец (от 1 до 3): ")) - 1

        if board[row][col] == ' ':
            board[row][col] = current_player
            turns += 1

            if check_row(row, current_player) or \
                    check_col(col, current_player) or \
                    check_diagonal(current_player):
                print_board()
                print(f"Игрок {current_player} победил!")
                return

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Это место занято. Выберите другое.")

    print_board()
    print("Игра окончилась. Ничья!")


play_game()
