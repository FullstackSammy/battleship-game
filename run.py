from random import randint

# This creates a board with 8 rows and columns
computer_board = [[" "] * 8 for x in range(8)]
# This creates a board with 8 rows and columns
guessing_board = [[" "] * 8 for i in range(8)]


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
    This function prints and displays the boards
    """
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1




def create_ships(board):
    """
    This function will generate and place out ships randomly on the boards.
    """
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"


def get_ship_location():
    """
    Asks the user for which row and column they want to guess where the ship is
    """
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
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
    create_ships(HIDDEN_BOARD)
    turns = 10
    while turns > 0:
        print('Guess a battleship location')
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "-":
            print("You guessed that one already.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("Hit")
            GUESS_BOARD[row][column] = "X" 
            turns -= 1  
        else:
            print("MISS!")
            GUESS_BOARD[row][column] = "-"   
            turns -= 1     
        if count_hit_ships(GUESS_BOARD) == 5:
            print("You win!")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("You ran out of turns")


if __name__ == "__main__":
    run_game()