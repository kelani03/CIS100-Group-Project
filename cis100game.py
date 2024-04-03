import random

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
            play_number_game(max_attempts)
        elif choice == "3":
            name = input("What is your name? ")
            print(f"Good Luck ! {name}")
            play_hangman_game()
        elif choice == "4":
            print("Exiting the Game Menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
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
            else:   # If the roll is odd
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
        
# Number Guessing Game Code
# ... (Number Guessing Game code remains the same) ...

# Hangman Game Code
# ... (Hangman Game code remains the same) ...


# Shape Mash Game
# ... (Shape Mash Game code goes here) ...