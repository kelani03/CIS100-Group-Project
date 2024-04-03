# Reference: https://github.com/username/repo_name

# Xs and Os

def main():
    # The main function
    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    symbol_1, symbol_2 = choose_symbols()
    full = is_full(board, symbol_1, symbol_2)  # The function that starts the game is also in here.


def intro():
    # This function introduces the rules of the Xs and Os game
    print("Welcome Competitors! Let's play Xs and Os!")
    print("\n")
    print("Rules: Gamers 1 and 2, symbolized by X and O, take turns placing their marks in a 3x3 grid.")
    print("The winner is the gamer who places three of their marks in a row, either horizontally, vertically, or diagonally.")
    print("\n")
    input("Press enter to continue.")
    print("\n")


def create_grid():
    # This function creates a blank playboard
    print("Here is the playboard:")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board


def choose_symbols():
    # This function allows the gamers to choose their symbols
    symbol_1 = input("Gamer 1, do you want to be X or O? ")
    if symbol_1 == "X":
        symbol_2 = "O"
        print("Gamer 2, you are O.")
    else:
        symbol_2 = "X"
        print("Gamer 2, you are X.")

    input("Press enter to continue.")
    print("\n")

    return symbol_1, symbol_2


def start_gamming(board, symbol_1, symbol_2, count):
    # This function starts the game.

    # Determines the current gamer’s turn based on the count
    if count % 2 == 0:
        current_gamer = symbol_1
    else:
        current_gamer = symbol_2

    print("Gamer " + current_gamer + ", it's your turn.")

    # Prompt the Gamer to choose a row and column
    row = int(input("Pick a row (0 for upper row, 1 for middle row, 2 for bottom row): "))
    column = int(input("Pick a column (0 for left column, 1 for middle column, 2 for right column): "))

    # Check if the gamer’s selection is out of range
    while row not in range(3) or column not in range(3):
        out_of_board(row, column)
        row = int(input("Pick a row (0 for upper row, 1 for middle row, 2 for bottom row): "))
        column = int(input("Pick a column (0 for left column, 1 for middle column, 2 for right column): "))

    # Check if the square is already filled
    while (board[row][column] == symbol_1) or (board[row][column] == symbol_2):
        illegal_move(board, symbol_1, symbol_2, row, column)
        row = int(input("Pick a row (0 for upper row, 1 for middle row, 2 for bottom row): "))
        column = int(input("Pick a column (0 for left column, 1 for middle column, 2 for right column): "))

    # Locates gamer's symbol on the board
    if current_gamer == symbol_1:
        board[row][column] = symbol_1
    else:
        board[row][column] = symbol_2

    return board


def is_full(board, symbol_1, symbol_2):
    count = 1
    winner = True
    # This function checks if the board is full
    while count < 10 and winner:
        gaming = start_gamming(board, symbol_1, symbol_2, count)
        pretty = printPretty(board)

        if count == 9:
            print("The board is full. Game over.")
            if winner:
                print("There is a tie.")

        # Check if there is a winner
        winner = is_winner(board, symbol_1, symbol_2, count)
        count += 1
    if not winner:
        print("Game over.")

    # This function gives a report
    report(count, winner, symbol_1, symbol_2)


def out_of_board(row, column):
    # This function notifies the players that their selection is out of range
    print("Out of bounds. Please pick another one.")


def printPretty(board):
    # This function prints the board in a nice format
    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board


def is_winner(board, symbol_1, symbol_2, count):
    # This function checks if any gamer has won
    winner = True
    # Check the rows
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print("Gamer " + symbol_1 + ", congratulations, you won!")
        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print("Gamer " + symbol_2 + ", congratulations, you won!")

    # Check the columns
    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print("Gamer " + symbol_1 + ", congratulations, you won!")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print("Gamer " + symbol_2 + ", congratulations, you won!")

    # Check the diagonals
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False
        print("Gamer " + symbol_1 + ", congratulations, you won!")
    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print("Gamer " + symbol_2 + ", congratulations, you won!")
    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print("Gamer " + symbol_1 + ", congratulations, you won!")
    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print("Gamer " + symbol_2 + ", congratulations, you won!")

    return winner


def illegal_move(board, symbol_1, symbol_2, row, column):
    print("The square you picked is already filled. Please pick another one.")


def report(count, winner, symbol_1, symbol_2):
    print("\n")
    input("Press enter to see the game summary. ")
    if (winner == False) and (count % 2 == 1):
        print("Winner: Gamer " + symbol_1 + ".")
    elif (winner == False) and (count % 2 == 0):
        print("Winner: Gamer " + symbol_2 + ".")
    else:
        print("It's a draw.")


# Call Main
main()





    



