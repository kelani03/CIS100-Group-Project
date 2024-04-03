import random

# Number Guessing Game Code
# define range and maximum of attempts. as well as storing variables to keep track of the
#user's score and the total number of games
lower = 1
upper = 50
max_attempts = 5
user_score = 0
total_games = 0

# generate answer
def play_number_game():
    global user_score, total_games
    answer = random.randint(lower, upper)

    # get user's response
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

    # answer validation
    def check_guess(guess, answer):
        if guess == answer:
            return "Correct"
        elif guess < answer:
            return "Too low, guess again."
        else:
            return "Too high, guess again."

    #plays the game. returns the number of attempts it took for the user to guess the correct number
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

    #asks the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        display_scores(user_score, total_games)
        return

    play_number_game()

#displays the user's score and the average number of attempts it took the user to guess the answer
def display_scores(user_score, total_games):
    if total_games > 0:
        avg_attempts = user_score/total_games
    else:
        print("You have not played any games yet.")
        return
    print (f"Your score is {user_score} out of {total_games} games. Average number of attempts it took you to guess the answer is {avg_attempts}.")

def main_menu():
    while True:
        print("\nWelcome to the Game Menu!")
        print("1. Dice Game")
        print("2. Number Guessing Game")
        print("3. Hangman Game")
        print("4. Shape Mash Game")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            play_dice_game()
        elif choice == "2":
            print("Welcome to the Number Guessing Game!")
            play_number_game()
        elif choice == "3":
            play_hangman_game()
        elif choice == "4":
            print("Exiting the Game Menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
# Dice Game Code
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
    print(f"Good Luck ! {name}")

    words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
    
    word = random.choice(words)
    print("Guess the characters")
    
    guesses = ''
    
    turns = 12
    
    while turns > 0:
        
        failed = 0
        
        for char in word:
            
            if char in guesses:
                print(char, end=" ")
            
            else:
                print("_")
                
                failed += 1
                
                if failed == 0:
                    print("You Win")
                    
                    print("The word is: ", word)
                    break
                
                print()
                guess = input("guess a character:")
                guesses += guess
                
                if guess not in word:
                    turns -= 1
                    
                    print("Wrong")
                    print("You have", + turns, 'more guesses')
                    
                    if turns == 0:
                        print("You Loose")
 


# Shape Mash Game
# ... (Shape Mash Game code goes here) ...

if __name__ == "__main__":
    main_menu()
