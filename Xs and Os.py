# Reference: https://github.com/username/repo_name

# Xs and Os

def main():
    # Main function
    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    symbol_1, symbol_2 = sym()
    full = isFull(board, symbol_1, symbol_2)  # The function that starts the game is also in here.
   

   


def intro():
    # This function introduces the rules of the game Tic Tac Toe
    print("Welcome Competitors! The Xs and Os game!")
    print("\n")
    print("Rules: Gamer 1 and gamer 2, represented by X and O, take turns "
          "marking the spaces in a 3*3 grid. The gamer who succeeds in placing "
          "three of their marks in a horizontal, vertical, or diagonal row wins.")
    print("\n")
    input("Press enter to continue.")
    print("\n")



def create_grid():
    # This function creates a blank grid
    print("Here is the grid: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board


def sym():
    # This function decides the gamers' symbols
    symbol_1 = input("Gamer 1, do you want to be X or O? ").upper()
    while symbol_1 not in ['X', 'O']:
        print("Invalid input. Please enter X or O.")
        symbol_1 = input("Gamer 1, do you want to be X or O? ").upper()

    symbol_2 = 'O' if symbol_1 == 'X' else 'X'
    print(f"Gamer 2, you are {symbol_2}.")
    input("Press enter to continue.")
    print("\n")
    return (symbol_1, symbol_2)





def startGamming(board, symbol_1, symbol_2, count):
    # This function starts the game.

    # Decides the turn
    if count % 2 == 0:
        gamer = symbol_1
    elif count % 2 == 1:
        gamer = symbol_2
    print("Gamer "+ gamer + ", it is your turn. ")
    row = int(input("Pick a row:"
                    "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
    column = int(input("Pick a column:"
                       "[left column: enter 0, middle column: enter 1, right column enter 2]"))


    # Check if gamers' selection is out of range
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outOfBoard(row, column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, right column enter 2]"))

        # Check if the square is already filled
    while (board[row][column] == symbol_1)or (board[row][column] == symbol_2):
        filled = illegal(board, symbol_1, symbol_2, row, column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                            "[left column: enter 0, middle column: enter 1, right column enter 2]"))    
       
    # Locates gamer's symbol on the board
    if gamer == symbol_1:
        board[row][column] = symbol_1
           
    else:
        board[row][column] = symbol_2
   
    return (board)



def isFull(board, symbol_1, symbol_2):
    count = 1
    winner = True
    # This function checks if the board is full
    while count < 10 and winner == True:
        gaming = startGamming(board, symbol_1, symbol_2, count)
        pretty = printPretty(board)
       
        if count == 9:
            print("The board is full. Game over.")
            if winner == True:
                print("There is a tie. ")

        # Check if there is a winner
        winner = isWinner(board, symbol_1, symbol_2, count)
        count += 1
    if winner == False:
        print("Game over.")
       
    # This is function gives a report
    report(count, winner, symbol_1, symbol_2)



def outOfBoard(row, column):
    # This function tells the gamers that their selection is out of range
    print("Out of boarder. Pick another one. ")
   
   

def printPretty(board):
    # This function prints the board nicely
    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board



def isWinner(board, symbol_1, symbol_2, count):
    # This function checks if any winner is winning
    winner = True
    # Check the rows
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print("Gamer " + symbol_1 + ", you won!")
   
        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print("Gamer " + symbol_2 + ", you won!")
           
           
    # Check the columns
    for col in range (0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print("Gamer " + symbol_1 + ", you won!")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print("Gamer " + symbol_2 + ", you won!")

    # Check the diagnoals
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False
        print("Gamer " + symbol_1 + ", congratulations! You won!")

    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print("Gamer " + symbol_2 + ", Congratulations! You won!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print("Gamer " + symbol_1 + ", Congratulations! You won!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print("Gamer " + symbol_2 + ", Congratulations! You won!")

    return winner
   


def illegal(board, symbol_1, symbol_2, row, column):
    # This function informs the gamers that the square they picked is already filled
    print("The square you picked is already filled. Pick another one.")

   
def report(count, winner, symbol_1, symbol_2):
    # This function gives a report on the game result
    print("\n")
    input("Press enter to see the game summary. ")
    if (winner == False) and (count % 2 == 1 ):
        print("Winner: Gamer " + symbol_1 + ".")
    elif (winner == False) and (count % 2 == 0 ):
        print("Winner: Gamer " + symbol_2 + ".")
    else:
        print("It's a draw ")





