import random
#library that we use in order to select something random

import colorama
from colorama import Fore, Back, Style

#initialize colorama 
colorama.init()

# Number Guessing Game Code
# define range and maximum of attempts. as well as storing variables to keep track of the
# user's score and the total number of games
lower = 1
upper = 50
max_attempts = 5
user_score = 0
total_games = 0

# this function allows the user to play the game
def play_number_game():
    global user_score, total_games
    
    #generates the answer
    answer = random.randint(lower, upper)

    # function that will the get user's response
    def get_guess():
        while True:
            try:
                guess = int(input(f"Guess the number between {lower} and {upper} : "))
                if lower <= guess <= upper:
                    return guess
                else:
                    print("Invalid input. Please re-enter.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # this function validates the guess 
    def check_guess(guess, answer):
        if guess == answer:
            return "Correct"
        elif guess < answer:
            return "Too low, guess again."
        else:
            return "Too high, guess again."

    # returns the number of attempts it took for the user to guess the correct number
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, answer)

        if result == "Correct":
            print(f"Congratulations, you have guessed the number {answer} in {attempts} attempts!")
            won = True
            break
        else:
            print (f"{result}. Try again!")

    if not won:
            print(f"Sorry, you ran out of attempts! The secret number is {answer}.")
    user_score += 1
    total_games += 1

    # asks the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        display_scores(user_score, total_games)
        return

    play_number_game()

# displays the user's score and the average number of attempts it took the user to guess the answer
def display_scores(user_score, total_games):
    if total_games > 0:
        avg_attempts = user_score/total_games
    else:
        print("You have not played any games yet.")
        return
    print (f"Your score is {user_score} out of {total_games} games. Average number of attempts it took you to guess the answer is {avg_attempts}.")

def main_menu():
    while True:
        print(Back.BLACK + Style.BRIGHT + Fore.WHITE + "--------------------------")
        print(Style.BRIGHT + Fore.BLUE + "WELCOME TO THE GAME MENU!")
        print(Style.BRIGHT + Fore.WHITE + "--------------------------")
        print(Style.BRIGHT + Fore.BLUE + "1. Dice Game")
        print(Style.BRIGHT + Fore.BLUE + "2. Number Guessing Game")
        print(Style.BRIGHT + Fore.BLUE + "3. Hangman Game")
        print(Style.BRIGHT + Fore.BLUE + "4. Xs and Os")
        print(Style.BRIGHT + Fore.BLUE + "5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            play_dice_game() + colorama.Fore.WHITE 
        elif choice == "2":
            print("Welcome to the Number Guessing Game!")
            play_number_game()
        elif choice == "3":
            play_hangman_game()
        elif choice == "4":
            introduction = intro()
            board = create_grid()
            pretty = printPretty(board)
            symbol_1, symbol_2 = sym()
            count = 1
            isFull(board, symbol_1, symbol_2)
        elif choice == "5":
            print("Exiting the Game Menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
# Dice Game Code
#Define the Player class
class Player:
    # Initializing player's name and position
    def __init__(self, name):
        self.name = name
        self.position = 0

    # Method to roll the dice
    def roll_dice(self):
        diceRoll = random.randint(1, 6)
        return diceRoll

# Define the game function
def play_dice_game():
    # Get the number of players from user input
    num_players = int(input("Enter the number of players: "))

    # Create Player objects with names entered by the user
    players = [Player(input(f"Enter player {i+1}'s name: ")) for i in range(num_players)]

    winner = None  # Initialize the winner to None

    # Game loop continue until we have a winner
    while winner is None:
        # Iterate through each player's turn
        for player in players:
            print(f"{player.name}, it's your turn")
            input("Press enter to roll the dice")
            roll = player.roll_dice()  # Roll the dice for the player

            print(f"{player.name} rolled a {roll}.")

            # Update player's position based on the dice roll
            if roll % 2 == 0:  # If the roll is even
                player.position += roll  # Increase player's position
                print(f"{player.name}, your position has increased. You are at position: {player.position}")
            else:  # If the roll is odd
                player.position -= roll  # Decrease player's position
                print(f"{player.name}, your position has decreased. You are at position: {player.position}")

            # Check if the player has gone below 0
            if player.position < 0:
                player.position = 0
                print(f"{player.name}, your position has fallen below 0. Your position has been corrected to: {player.position}")

            # Check if the player has won
            if player.position >= 20:
                winner = player
                print(f"{player.name} is now on position {player.position}.\n")
                print(f"Congratulations, {player.name}! You won the game.")
                break

    print("\nFinal Positions:")
    for player in players:
        print(f"{player.name}: {player.position}")


# Hangman Game Code
def play_hangman_game():
    name = input("What is your name? ")
    # Here the user is asked to enter the name first
    
    print(f"Good Luck ! {name}")

    words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
    
    # Function will choose one random word from this list of words
    word = random.choice(words)
    print("Guess the characters")
    
    guesses = ''
    
    # any number of turns can be used here
    turns = 12
    
    while turns > 0:
        
        # counts the number of times a user fails
        failed = 0
        
        # all characters from the input word taking one at a time
        for char in word:
            
            # comparing that character with the character in guesses
            if char in guesses:
                print(char, end=" ")
            else:
                print("_")
               
               # for every failure 1 will be incremented in failure 
                failed += 1
                
                if failed == 0:
                    # user will win the game if failure is 0
                    # and 'You Win' will be given as output
                    print("You Win")
                    
                    # this prints the correct word
                    print("The word is: ", word)
                    break
                
                # if user has input the wrong alphabetthen it will ask the user to enter another alphabet
                print()
                guess = input("guess a character:")
                
                # every input character will be stored in guesses
                guesses += guess
                
                if guess not in word:
                    turns -= 1
                    
                    # if the character doesn't match the word then "Wrong will be given as output
                    print("Wrong")
                    print("You have", + turns, 'more guesses')
                    
                    if turns == 0:
                        print("You Loose")
 


# Xs and Os Game
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


def isBoardFull(board):
    #this function checks if the board is full
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return False
    return True

def isFull(board, symbol_1, symbol_2):
    count = 1
    winner = True
    # This function checks if the board is full
    
    while count < 10 and winner == True:
        gaming = startGamming(board, symbol_1, symbol_2, count)
        pretty = printPretty(board)
       

        # Check if there is a winner
        winner = isWinner(board, symbol_1, symbol_2, count)
        if winner == False:
            print("Game over.")
            break
        
        #Check if the board is full
        if isBoardFull(board):
            print("The board is full. Game over.")
            print("There is a tie.")
            break #exit the loop if the board is full
        
        count += 1
       
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

# Call Main

if __name__ == "__main__":
    main_menu()
