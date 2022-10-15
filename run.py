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


player_score = 0
computer_score = 0


continue_game = ['y', 'yes', 'n', 'no']


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
    It generates an integer with random int between 0 and 7 for the row and column
    """
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "@":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = "@"


def computer_guess(board):
    global computer_score
    computer_row, computer_column = randint(0, 7), randint(0, 7)
    if (player_board[computer_row][computer_column] == "-" or
            player_board[computer_row][computer_column] == "X"):
        computer_row = randint(0, 7)
        computer_column = randint(0, 7)
    elif player_board[computer_row][computer_column] == "@":
        print(f'Oh no {username}! One of you ships went down!')
        print(f'The computer guessed row {computer_row +1} and column {computer_column}')
    else:
        print(f'The computer missed. Get him next turn {username}.')
        print(f'Oh no {username}! One of you ships went down!')
        print(f'The computer guessed row {computer_row +1} and column {computer_column}')
        player_board[computer_row][computer_column] = "-"

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
