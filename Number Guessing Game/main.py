import random
from art import logo

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5

def guessing(user_guess, actual_number, lives):
    if user_guess > actual_number:
        print("Too high!")
        return lives - 1
    elif user_guess < actual_number:
        print("Too low!")
        return lives - 1
    else:
        print(f"Well done! The number was {actual_number}")



def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_DIFFICULTY
    else:
        return HARD_DIFFICULTY

def play_game():
    print(logo)
    print("Welcome to the random number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1, 100)

    lives = set_difficulty()
    print(f"You have {lives} guesses left.")

    guess = 0
    while guess != random_number:
        guess = int(input("Make a guess... "))

        guessing(guess, random_number, lives)
        if lives == 0:
            print("You lose!")
            return

