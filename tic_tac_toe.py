import os
import time
import math


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
                if not is_valid_move(board, row, col):
                    raise ValueError
                is_not_valid = False
            except TypeError and ValueError:
                print("Given the wrong coordinates.")
        else:
            print("It doesn't look like the board coordinates.")
    return (row, col)


def minmax(board, player, depth, is_maximazing):
    opponent = "0" if player == "X" else "X"

    if has_won(board, player):
        return 1
    elif has_won(board, opponent):
        return -1
    elif is_full(board):
        return 0

    if is_maximazing:
        best_score = -math.inf
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    mark(board, player, (i, j))
                    score = minmax(board, player, depth+1, False)
                    board[i][j] = "."
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    mark(board, opponent, (i, j))
                    score = minmax(board, player, depth+1, True)
                    board[i][j] = "."
                    best_score = min(score, best_score)
        return best_score


def get_ai_move(board, computer):
    """Returns the coordinates of a valid move for player on board."""
    best_score = -math.inf
    best_move = None

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ".":
                mark(board, computer, (i, j))
                score = minmax(board, computer, 0, False)
                board[i][j] = "."
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    mark(board, computer, best_move)


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
    print("The End")
    if winner in ["X", "0"]:
        print(f"{winner} has won!")
    elif winner == "T":
        print("It's a tie!")


def human_human_mode(board):
    player = "X"
    winner = None

    while not winner:
        if is_full(board):
            winner = "T"
        else:
            print(f"Player's {player} turn")
            move = get_move(board)
            if not move:  # player typed "quit"
                break
            mark(board, player, move)
            print_board(board)

            if has_won(board, player):
                winner = player
            else:
                player = "0" if player == "X" else "X"
    print_result(winner)


def human_ai_mode(board, human_turn):
    player = "0"
    human_sign = ["0", "X"][human_turn]
    ai_sign = "0" if human_sign == "X" else "X"
    winner = None

    while not winner:
        if is_full(board):
            winner = "T"
        else:
            print(f"Player's {player} turn")
            if player == human_sign:
                move = get_move(board)
                if not move:
                    break
                mark(board, player, move)
            elif player == ai_sign:
                time.sleep(1)
                get_ai_move(board, player)
            print_board(board)

            if has_won(board, player):
                winner = player
            else:
                player = "0" if player == "X" else "X"
    print_result(winner)


def ai_ai_mode(board):
    player = "0"
    winner = None

    while not winner:
        if is_full(board):
            winner = "T"
        else:
            print(f"Player's {player} turn")
            time.sleep(1)
            get_ai_move(board, player)
            print_board(board)

            if has_won(board, player):
                winner = player
            else:
                player = "0" if player == "X" else "X"
    print_result(winner)


def tictactoe_game(mode="HUMAN-HUMAN", board_size=3):
    board = init_board(board_size)
    print_board(board)

    if mode == "HUMAN-HUMAN":
        human_human_mode(board)
    elif mode == "HUMAN-AI":
        human_ai_mode(board, 0)
    elif mode == "AI-HUMAN":
        human_ai_mode(board, 1)
    elif mode == "AI-AI":
        ai_ai_mode(board)


def get_option(text, options):
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


def get_str_input_mode(modes):
    str_input_mode = ""
    for i in range(1, len(modes)+1):
        str_input_mode += f"{i}) \"{modes[i-1]}\" mode\n"
    str_input_mode += "\nChoose mode: "
    return str_input_mode


def main_menu():
    is_not_valid = True

    while (is_not_valid):
        os.system("cls || clear")
        modes = ["HUMAN-HUMAN", "HUMAN-AI", "AI-HUMAN", "AI-AI"]
        str_input_mode = get_str_input_mode(modes)

        print("Tic Tac Toe\n")
        input_mode = get_option(str_input_mode, range(1, len(modes)+1))

        if input_mode in range(1, len(modes)+1):
            board_size = get_option("Enter board size (3-5): ", [3, 4, 5]) if input_mode == 1 else 3
            mode = modes[input_mode-1]
            print(f"You've chosen mode {mode}")
            time.sleep(2)
            tictactoe_game(mode, board_size)
            is_not_valid = False
        else:
            print("You didn't select valid mode")


if __name__ == '__main__':
    main_menu()
