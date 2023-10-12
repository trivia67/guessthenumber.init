#

import random
from art import logo

easy_level_turns = 10
hard_level_turns = 5

# 4. function to check the guess against the actual answer


def check_answer(guess_number, random_number, turns):
    if guess_number > random_number:
        print("Too High")
        return turns-1
    elif guess_number < random_number:
        print("Too Low")
        return turns-1
    else:
        print(f"You got it. The correct answer is {random_number}")

# 2. Make function to set difficulty


def difficulty_level():
    user_level = input("Choose difficulty. Type 'easy' for easy level and 'hard' for hard level:").lower()
    if user_level == 'easy':
        return easy_level_turns
    elif user_level == 'hard':
        return hard_level_turns

# 1. choosing a random number between 1 and 100.


def game():
    print(logo)
    random_number = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    print(f"pssst.... the number is {random_number}")
    turns = difficulty_level()

    # 6. Repeat the guessing functionality if they get it wrong
    guess_number = 0
    while guess_number != random_number:
        print(f"You have {turns} attempts remaining to guess the number")

        # 3. ask the user to guess the number
        guess_number = int(input("Guess the number:"))
        # 5. Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess_number, random_number, turns)
        if turns == 0:
            print("You have run out of guesses! You lose")
            return
        elif guess_number!= random_number:
            print("Guess again")

game()


