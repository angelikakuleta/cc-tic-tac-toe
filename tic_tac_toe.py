import os


def init_board(size):
    """Returns an empty board (with .)."""
    board = []
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append('.')
    return board


def is_valid_move(board, row, col):
    length = len(board)
    if row >= length or row < 0:
        return False
    if col >= length or col < 0:
        return False
    if board[row][col] != '.':
        return False
    return True


def get_move(board):
    """Returns the coordinates of a valid move for player on board."""
    row_coords = "ABCDE"
    row, col = 0, 0
    is_not_valid = True

    while (is_not_valid):
        player_input = input("Enter the board coordinates or 'quit' to leave: ").upper()

        if player_input == "QUIT":
            print('Good bye')
            return None
        elif (len(player_input) == 2 and player_input.isalnum()):
            try:
                row = row_coords.index(player_input[0])
                col = int(player_input[1]) - 1
                if (is_valid_move(board, row, col)):
                    raise ValueError
                is_not_valid = False
            except TypeError or ValueError:
                print("Given the wrong coordinates.")
        else:
            print("It doesn't look like the board coordinates.")
    return (row, col)


# TODO get_ai_move function
def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, sign, coordinates):
    """Marks the element at row & col on the board for player."""
    row = coordinates[0]
    col = coordinates[1]
    try:
        if (board[row][col] == "."):
            board[row][col] = sign
        else:
            print("This field is taken")
    except IndexError:
        print("Given the wrong coordinates")


def is_horizontal_identical(board, sign):
    length = len(board)
    for i in range(length):
        for j in range(length):
            if board[i][j] != sign:
                break
        else:  # only executed if the inner loop did NOT break
            return True
    return False


def is_vertical_identical(board, sign):
    length = len(board)
    for j in range(length):
        for i in range(length):
            if board[i][j] != sign:
                break
        else:
            return True
    return False


def is_diagonal_left_identical(board, sign):
    length = len(board)
    for i in range(length):
        if board[i][i] != sign:
            break
    else:
        return True
    return False


def is_diagonal_right_identical(board, sign):
    length = len(board)
    for i in range(length):
        if board[length-1-i][i] != sign:
            break
    else:
        return True
    return False


def has_won(board, sign):
    """Returns True if player has won the game."""
    is_identical = False

    if is_horizontal_identical(board, sign):
        is_identical = True
    elif is_vertical_identical(board, sign):
        is_identical = True
    elif is_diagonal_left_identical(board, sign):
        is_identical = True
    elif is_diagonal_right_identical(board, sign):
        is_identical = True
    return is_identical


def is_full(board):
    """Returns True if board is full."""
    for row in board:
        if "." in row:
            return False
    return True


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    length = len(board)
    row_coords = "ABCDE"

    os.system("cls || clear")
    print()
    print(" ", end="")
    for i in range(length):
        print(f" | {i+1}", end="")
    print()
    for i in range(length):
        print("--", end="")
        for j in range(length):
            print("+---", end="")
        print()
        print(f"{row_coords[i]} | " + " | ".join(board[i]))
    print()


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner in ["X", "0"]:
        print(f"{winner} has won!")
    elif winner == "T":
        print("It's a tie!")


def human_human_mode(board):
    player = "X"
    winner = None

    while not winner:
        if is_full(board):
            print("The End")
            winner = "T"
            print_result(winner)
        else:
            print(f"Player's {player} turn")
            move = get_move(board)
            if not move:  # player typed "quit"
                break
            mark(board, player, move)
            print_board(board)

            if has_won(board, player):
                winner = player
                print("The End")
                print_result(winner)

            player = "0" if player == "X" else "X"


def tictactoe_game(mode='HUMAN-HUMAN', board_size=3):
    board = init_board(board_size)
    print_board(board)

    if mode == 'HUMAN-HUMAN':
        human_human_mode(board)

    # TODO game logic for HUMAN-AI and AI-HUMAN mode
    elif mode == 'HUMAN-AI':
        pass


def give_option(text, options):
    is_valid_option = False
    player_input = None
    while not is_valid_option:
        try:
            player_input = int(input(text))
            if player_input in options:
                is_valid_option = True
            else:
                raise ValueError
        except TypeError and ValueError:
            print("Given the wrong option\n")
    return player_input


def main_menu():
    is_not_valid = True

    while (is_not_valid):
        os.system("cls || clear")
        input_mode = give_option('1) "2-player mode"\n2) "player against-AI mode"\n\nChoose mode: ', [1, 2])
        board_size = give_option("Enter board size (3-5): ", [3, 4, 5])

        if input_mode == 1:
            mode = 'HUMAN-HUMAN'
            print(f"You've chosen mode {mode}")
            tictactoe_game(mode, board_size)
            is_not_valid = False
        elif input_mode == 2:
            mode = 'HUMAN-AI'
            print(f"You've chosen mode {mode}")
            tictactoe_game(mode, board_size)
            is_not_valid = False
        else:
            print("You didn't select valid mode")


if __name__ == '__main__':
    main_menu()
