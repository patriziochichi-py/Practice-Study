# Create a higher or lower game
# the game has to compare 2 different celebrities
# the user chooses who he thinks has the most followers
# if the user guesses wrong, the game ends
# if the user guesses right, the game keeps on going and asks again
# when the user guess is right his score goes up
# the two celebrities are divided in A and B
# after the guess, B becomes A and gets compared to a new B

# TODO 1: The game starts and prints the logo. O
# TODO 2: The game immediately compares celeb A with celeb B 0
# TODO 3: The user guesses who has more followers by inputting A or B 0
# TODO 4: The game has to compare the followers 0
# TODO 5: If correct the score goes up and then B becomes A and is compared with a new B
# TODO 6: If the guess is wrong, the game ends

from game_data import data
from art import logo, vs
import random

def choose_celebrity():
    return random.choice(data)


def celeb_values(celeb):
    return [value for key, value in celeb.items() if key != "follower_count"]

def format_data(celeb):
    celeb_name = celeb["name"]
    celeb_description = celeb["description"]
    celeb_country = celeb["country"]
    return f"{celeb_name}, {celeb_description}, from {celeb_country}"


def play_game():
    game_over = False
    score = 0
    random_celeb_b = choose_celebrity()

    while not game_over:
        random_celeb_a = random_celeb_b
        random_celeb_b = choose_celebrity()


        print(logo)
        highest_followers = max(random_celeb_a["follower_count"], random_celeb_b["follower_count"])
        print(f" Compare A: {format_data(random_celeb_a)}")
        print(vs)
        print(f" Compare B: {format_data(random_celeb_b)}")

        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_guess == "A".lower():
            if random_celeb_a["follower_count"] == highest_followers:
                score += 1
                print(f"You're right! Current score: {score}")
            else:
                game_over = True
                print(f"Sorry, that's wrong. Final score: {score}")

        if user_guess == "B".lower():
            if random_celeb_b["follower_count"] == highest_followers:
                score += 1
                print(f"You're right! Current score: {score}")
            else:
                game_over = True
                print(f"Sorry, that's wrong. Final score: {score}")

play_game()
