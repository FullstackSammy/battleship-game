from random import randint

# Legend
# "@" for placing ship
# " " for available space
# "X" for battleships hit
# "-" for battleships missed

# This creates a board with 8 rows and columns
computer_board = [[" "] * 8 for x in range(8)]
# This creates a board with 8 rows and columns
guessing_board = [[" "] * 8 for i in range(8)]
# This creates a board with 8 rows and columns
player_board = [[" "] * 8 for i in range(8)]


# This converts letters into numbers
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}


def print_board(board):
    """
    This function prints and displays the boards.
    numbers for rows and letters for columns
    """
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print(row_number, "|".join(row))
        row_number += 1


def create_ships(board):
    """
    This function will generate and place out ships randomly on the boards.
    """
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"


def get_ship_location():
    """
    Asks the user for which row and column they want to guess where the ship is
    """
    row = input("Enter the row of the ship (1-8): ").upper()
    while row not in "12345678":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship (1-8): ").upper()
    column = input("Enter the column of the ship (A-H): ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship (A-H): ").upper()
    return int(row) - 1, letters_to_numbers[column]


def count_hit_ships(board):
    """
    This will count each hit you get. If you get all five
    The game is over.
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


def run_game():
    """
    This function runs starts the game.
    """
    create_ships(computer_board)
    turns = 10
    print("Welcome to Battleships")
    while turns > 0:
        print('Guess a location for enemy ship')
        print_board(guessing_board)
        row, column = get_ship_location()
        if guessing_board[row][column] == "-":
            print("That guess has already been made")
        elif guessing_board[row][column] == "X":
            print("Well done! You sunk an enemy ship!")
            guessing_board[row][column] = "X"
            turns -= 1
        else:
            print("Aw, you missed. try again!")
            guessing_board[row][column] = "-"
            turns -= 1
        if count_hit_ships(guessing_board) == 5:
            print("Congratulations! You win the game!")
            break
        print(f'You have {turns} turns left!')
        if turns == 0:
            print("You ran out of turns. Game over")


run_game()
