# TODO add expandable board
def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    return board


# TODO handle errors
def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    col_coords = "abc"
    row, col = 0, 0
    is_not_valid = True

    while (is_not_valid):
        player_input = input("Enter the board coordinates: ").lower()

        if (len(player_input) == 2 and player_input.isalnum()):
            try:
                row = col_coords.index(player_input[0])
                col = int(player_input[1]) - 1
                if (row >= 3 or col >= 3):
                    raise ValueError
                # TODO check if the player has provided coordinates for a place that is taken

                is_not_valid = False
            except TypeError and ValueError:
                print("Given the wrong coordinates.")
        else:
            print("It doesn't look like the board coordinates.")

    return (row, col)


# TODO get_ai_move function
def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    sign = ["X", "0"][player]
    try:
        if (board[row][col] == "."):
            board[row][col] = sign
        else:
            pass
    except IndexError:
        pass


# TODO has_won function
def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
    for row in board:
        if "." in row:
            return True
    return False


# TODO modify to flexible board printing
def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    print("   1   2   3")
    print("A  ", end="")
    print(" | ".join(board[0]))
    print("  ---+---+---")
    print("B  ", end="")
    print(" | ".join(board[1]))
    print("  ---+---+---")
    print("C  ", end="")
    print(" | ".join(board[2]))
    print("  ---+---+---")


# TODO print_result function
def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


# TODO game logic for HUMAN-HUMAN mode
# TODO game logic for HUMAN-AI and AI-HUMAN mode
# TODO game logic for AI-AI mode
def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)
    print_board(board)

    winner = 0
    print_result(winner)


# TODO menu for between choosing 2-player mode and against-AI mode by pressing 1 or 2
def main_menu():
    tictactoe_game('HUMAN-HUMAN')


# TODO quit game anytime by typing "quit"
# TODO add ASCII art


if __name__ == '__main__':
    main_menu()
