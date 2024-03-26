import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def roll_dice(self):
        diceRoll = random.randint(1, 6)  
        return diceRoll

def play_game():

    num_players = int(input("Enter the number of players: "))
    
    players = [Player(input(f"Enter player {i+1}'s name: ")) for i in range(num_players)]
    
    winner = None  
    
    while winner is None:
        
        for player in players:
            print(f"{player.name}, it's your turn")
            input("Press enter to roll the dice")
            roll = player.roll_dice()  
            
            print(f"{player.name} rolled a {roll}.")
        
            if roll % 2 == 0:  
                player.position += roll  
                print(f"{player.name}, your position has increased. You are at position: {player.position}")
            else:  
                player.position -= roll  
                print(f"{player.name}, your position has decreased. You are at position: {player.position}")
            
            if player.position < 0:  
                player.position = 0  
                print(f"{player.name}, your position has fallen below 0. Your position has been corrected to: {player.position}")
            
            if player.position >= 20:  
                winner = player  
                print(f"{player.name} is now on position {player.position}.\n")
                print(f"Congratulations, {player.name}! You won the game.")
                break  
    
    print("\nFinal Positions:")
    for player in players:
        print(f"{player.name}: {player.position}")

play_game()

