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