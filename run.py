hidden_board = [[' '] * 8 for x in range(8)]
# This creates a board with 8 rows and columns
guessing_board = [[' '] * 8 for x in range(8)]
# This creates a board with 8 rows and columns

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 
                      'F': 5, 'G': 6, 'H': 7}
# This converts letters into numbers


def print_board(board):
    """
    This function prints and displays the boards
    """
    print('A B C D E F G H')
    print('---------------')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


def create_ships():
    """
    This function will generate and place out ships randomly on the boards.
    """


def get_ship_location():
    """
    Asks the user for what row and column they want to guess where the ship is
    """
    pass


def count_hit_ships():
    """
    This will count each hit you get. If you get all five
    The game is over.
    """
    pass

