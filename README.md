# Battleships Game | Portfolio Project 3 - Code Institute
[Live Project](https://fullstacksammy-battleships.herokuapp.com/)

The all time classic Battleships game is a fun game that runs in a Python terminal. It runs in the Code Institute mock terminal on Heroku.
The player has 10 turns to sink all the enemy ships (the computer is the enemy). There are 5 battleships that occupy a single space on the board.

![repsonsiveness of the game](/assets/images/responsive.jpg)

## How to play

The player enters their name and two boards are randomly generated. The first board displayed is the player’s board which shows the locations of the ships which the computer needs to find. The second board is the computer’s board which is where the players’s guesses will be updated, this will not show the ship locations until the player has hit one of the ships. If a guess misses a battleship, then a - will be display, when a battleship has been hit “X” will be displayed. You win if you get all 5 enemy ships before your 10 turns run out. You lose if the computer sinks all your ships.

## User Stories

Create a Python game of battleships, where the player goes up against the computer.

- Display Game
- Display information about the game
- The user enters their name
- Two boards are displayed. One for user and one for computer
- The user enters his/her guess for row and column
- The users input guesses are checked against the hidden board
- A message to user to display if their guess was a hit or a miss
- The computer guesses are randomly generated
- The computer guesses are checked against the user board
- A message to user to display if the computer guess was a hit or miss
- The user and computer scores calculated and printed to terminal
- Turns remaining are printed to the terminal
- Continue playing option for the user to input y/n
- Users board updated with hit or miss and re-printed
- Computers board updated with hit or miss and re-printed
- If the user or computer has hit 5 ships, the relevant end game message is printed and program stops running
- If the user has run out of turns display message and end game

## Features

### Existing features

- Random board generation that displays for user and easy to read.
- A game to play against the computer
- Maintains scores throughout the game
- Try and except checking for input
- The computers guesses are randomised with the import of randint from random

In this game of Battleships, the player and computer each have up to 10 turns to find the opponents 5 battleships, and the winner if whoever finds all 5 first.

Each board has 8 rows and 8 columns, the rows are 1 to 8, and the columns are A to H.

Each battleship occupies one cell, and before the game starts, the computer generates the position of 5 battleships that the player and computer need to find to win.

The Player enters a ship row and column, and the computer generates a ship row and column.

If the players row and column does not find a battleship on the computers hidden board, there will be a message displayed and the location of the displayed computer board is marked with a -. The same goes for the computers guesses

If the player row and column does find a battleship on the computers hidden board, there will be a message displayed and the location of the displayed computer board is marked with an X. The same goes for the computers guesses

## Testing

Since the [PEP8 website](http://pep8online.com/) is down, I used the installed pep in the gitpod workspace to check my code and it passes.
 - I checked all the errors/problems and fixed them
 - Continuos testing of the project, to detect any bugs.

When the game is started a welcome message is displayed with the following info:
- A welcome message
- Quick explanation to the game
- An input box to put your name in and start the game
- You have to enter a string or an error message will show (see second img)

![startscreen](/assets/images/start.jpg)

![error message for name input](/assets/images/error-user.jpg)

When the game is started the boards are generated and displayed to the user. They include:
- Rows and columns with clear readability
- "@" markers for where your ships are
- input area where you put your guesses

![board screen]()

If you enter an invalid input ( not an integer or not a letter) when you make your guess. the following errors will show:

![board error]()

Once you get things right and make a correct guess. The computer will start to calculate and see if either of you got a hit.
Messages will be displayed and a continue to play option will appear. For example:

![continue playing]()

this also needs a valid input to work. Or you will get the following error:

![continue error]()

After a round, and you decided to continue playing, a newly generated board is shown with updated information about where you hits and misses are located.

![hit/miss location]()

When the user hit all 5 ships and wins, a congratulations-message appears and the game ends. The same goes if the computer wins.

## Bugs

