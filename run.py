from random import randint


# Legend
# "@" for placing ship
# " " for available space
# "X" for hit battleship
# "-" for missed shot


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


def create_ships(board):
    """
    This function will generate and place out ships randomly on the boards.
    """
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
    while board[ship_row][ship_column] == 'X':
        ship_row, ship_column = randint(0, 7), randint(0, 7)
    board[ship_row][ship_column] = 'X'


def get_ship_location():
    """
    Asks the user for which row and column they want to guess where the ship is
    """
    row = input('Please enter a row, 1-8: ')
    while row not in '12345678':
        print('Please enter a valid row')
        row = input('Please enter a row, 1-8: ')
        column = input('Please enter a column, 1-8: ').upper()
    while row not in 'ABCDEFGH':
        print('Please enter a valid row')
        row = input('Please enter a row, 1-8: ')
        return int(row) - 1, letters_to_numbers[column]  


def count_hit_ships():
    """
    This will count each hit you get. If you get all five
    The game is over.
    """
    

