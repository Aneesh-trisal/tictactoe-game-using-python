PLAYER_X = "X"
PLAYER_O = "O"
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
currentPlayer = PLAYER_X
winner = None
gameRunning = True

# Function to print the game board
def printBoard(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to take player input
def playerInput(board):
    while True:
        try:
            inp = int(input(f"Enter a number 1-9 for Player ({currentPlayer}) : "))
            if inp < 1 or inp > 9:
                print("Invalid input! Please enter a number between 1 and 9.")
            elif board[inp - 1] != "-":
                print("That spot is already taken! Try again.")
            else:
                board[inp - 1] = currentPlayer
                break
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")

# Functions to check win conditions
def checkHorizontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[0] != "-"):
        winner = currentPlayer
        return True
    elif (board[3] == board[4] == board[5] and board[3] != "-"):
        winner = currentPlayer
        return True
    elif (board[6] == board[7] == board[8] and board[6] != "-"):
        winner = currentPlayer
        return True

def checkRow(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "-"):
        winner = currentPlayer
        return True
    elif (board[1] == board[4] == board[7] and board[1] != "-"):
        winner = currentPlayer
        return True
    elif (board[2] == board[5] == board[8] and board[2] != "-"):
        winner = currentPlayer
        return True

def checkDiagonal(board):
    global winner
    if (board[0] == board[4] == board[8] and board[0] != "-"):
        winner = currentPlayer
        return True
    elif (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = currentPlayer
        return True

# Function to check for tie
def checkTie(board):
    global gameRunning
    if "-" not in board and winner is None:
        printBoard(board)
        print("It's a tie!")
        gameRunning = False

# Function to check if someone won
def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        printBoard(board)
        print(f"Congratulations! Player {winner} wins!")

# Function to switch players
def switchPlayer():
    global currentPlayer
    if currentPlayer == PLAYER_X:
        currentPlayer = PLAYER_O
    else:
        currentPlayer = PLAYER_X

# Function to restart the game
def restartGame():
    global board, currentPlayer, winner, gameRunning
    board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    currentPlayer = PLAYER_X
    winner = None
    gameRunning = True
    print("\nNew Game Started!\n")

# Main game loop
while gameRunning:
    print(f"It's {currentPlayer}'s turn")
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()

    # Check if the game is over and ask if the player wants to restart
    if winner or not gameRunning:
        play_again = input("Do you want to play again? (Y/N): ").lower()
        if play_again == 'y':
            restartGame()
        else:
            gameRunning = False
