# tictactoe-game-using-python

Tic-Tac-Toe (Python Console Version)
This is a simple command-line implementation of the classic Tic-Tac-Toe game using Python. It allows two players to take turns and play the game in the terminal.

How It Works:
The game board is a list of 9 elements representing 3x3 grid cells.
Players X and O take turns selecting positions 1 through 9.
The game checks for a win (horizontal, vertical, diagonal) or tie after each move.
Players are prompted to play again after a game ends.

How to Run:
Requires Python 3.x
Run the game using the command:
            python tictactoe.py

Main Features:
Input validation to prevent invalid or duplicate moves
Automatic win and tie detection
Option to restart the game
Turn-based two-player logic

Functions Overview:
printBoard(board): Renders the game board in console
playerInput(board): Gets and processes input from the current player
checkWin(): Checks all possible win conditions
checkTie(board): Ends the game if the board is full and there's no winner
switchPlayer(): Alternates turns between players
restartGame(): Resets the game state for a new round           
