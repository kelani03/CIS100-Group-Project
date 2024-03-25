import random

# define range and maximum of attempts. as well as storing variables to keep track of the
#user's score and the total number of games
lower = 1
upper = 50
max_attempts = 5
attempts = 0
user_score = 0
total_games = 0

# generate answer
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
def play_game(max_attempts):
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
    global user_score, total_games
    user_score += 1
    total_games += 1
    return attempts

#displays the user's score and the average number of attempts it took the user to guess the answer
def display_scores(user_score, total_games):
    if total_games > 0:
        avg_attempts = user_score/total_games
    else:
        print("You have not played any games yet.")
        return
    print (f"Your score is {user_score} out of {total_games} games. Average number of attempts it took you to guess the answer is {avg_attempts}.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")

    #play multiple games
    while True:
        play_game(max_attempts)

        #asks the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    #shows the user's score and avg attemots
    display_scores(user_score, total_games)