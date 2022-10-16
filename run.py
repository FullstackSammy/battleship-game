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
    Generates an integer with random int between 0 and 7 for the row and column
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
        print(f"Oh no {username}! One of you ships went down!")
    else:
        print('The computer missed.')
        player_board[computer_row][computer_column] = "-"


def try_row(values):
    """
    Prints an error message if values entered are not an integer between 1-8
    """
    try:
        [int(value) for value in values]
        if int(values) < 1 or int(values) > 8:
            print(
                f"Number between 1-8 required, you provided '{values}'."
            )
    except TypeError:
        print("Sorry number between 1-8 required, please try again.\n")
        return False

    return True


def try_column(values):
    """
    Prints an error message if values entered are not in letters_to_numbers
    """
    try:
        if values not in letters_to_numbers:
            print(
                f"Letter between A-H required, you provided '{values}'."
                )
    except TypeError:
        print("Sorry letter between A-H required, please try again.")
        return False

    return True


def get_ship_location():
    """
    Asks the user for which row and column they want to guess where the ship is
    checks the input data for row and columns
    returns integer for row and converts letters to numbers for column
    """
    row = input("Enter the row of the ship (1-8): ").upper()
    while row not in "12345678":
        try_row(row)
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship (1-8): ").upper()
    column = input("Enter the column of the ship (A-H): ").upper()
    while column not in "ABCDEFGH":
        try_column(column)
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


def start_screen():
    """
    This function is the main starting page. 
    It welcomes you to the game with a short explanation.
    Requires you to enter a username to start the game.
    """
    create_ships(computer_board)
    create_ships(player_board)
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print(" Welcome to Battleships")
    print(" You have 10 turns to find all of the battleships")
    print(" there are 8 rows and 8 columns")
    print(" Good luck!")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    global username
    username = input("Please enter your name:\n")
    while username == "" or username == " ":
        print("Sorry, please can you enter a name.")
        username = input("Please enter your name:\n")


def try_continue_game(values):
    """
    prints a TypeError if values entered are not in continue_game
    """
    try:
        if values not in continue_game:
            print(
                f"Please enter y/n, you provided '{values}'."
                )
    except TypeError:
        print('Sorry y/n required, please try again.')
        return False

    return True


def run_game():
    """
    This function runs the game.
    player has 10 turns and when 0, game over
    """
    turns = 10
    global player_score

    while turns > 0:
        print(f"{username}'s Board")
        print_board(player_board)
        print("Computer's Board")
        print_board(guessing_board)
        row, column = get_ship_location()
        if guessing_board[row][column] == "-" or guessing_board[row][column] == "X":
            print("You have already guessed that")
        elif computer_board[row][column] == "@":
            print(f"Well done {username}! You have sunk an enemy ship!")
            guessing_board[row][column] = "X"
            turns -= 1
            computer_guess(player_board)
            player_score += 1
        else:
            print(f"Sorry, you missed! Get him next turn {username}.")
            guessing_board[row][column] = "-"
            turns -= 1
            computer_guess(player_board)
        if count_hit_ships(guessing_board) == 5:
            print(
                f"Congratulations {username}, "
                "you have sunk all of the enemy battleships!")
            print("The game is now over")
            break
        print("You have " + str(turns) + " turns remaining")
        print(f"{username}'s Score: {player_score}")
        print(f"Computer's Score: {computer_score}")
        if turns == 0:
            print(
                f"Sorry {username}. You ran out of turns. The game is over")
            break
        if count_hit_ships(player_board) == 5:
            print(
                f"Sorry {username}, the computer"
                " has sunk all of your battleships")
            break
        if count_hit_ships(guessing_board) < 5:
            continue_playing = input(
                    "Do you want to continue playing? y/n \n").lower()
            while continue_playing not in continue_game:
                try_continue_game(continue_game)
                continue_playing = input(
                    "Do you want to continue playing? y/n\n").lower()
            if continue_playing == "y" or continue_playing == "yes":
                print(
                    "You have decided to continue playing the game.")
                continue
            elif continue_playing == "n" or continue_playing == "no":
                print(
                    "You have decided to stop playing, the game is now over")
                break
            else:
                print("Sorry, can you please enter y/n")
                continue_playing = input(
                    "Do you want to continue playing? y/n \n")


start_screen()
run_game()
