import random
import Number_art

print(Number_art.logo)

GAME_OVER = False
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def check_answer(guess, answer, attempts):
    if guess > answer:
        print("Too high!")
        return attempts - 1
    elif guess < answer:
        print("Too low!")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}")


def choose_difficulty():
    difficulty = input("Choose a difficulty: 'easy' or 'hard: ").lower()
    if difficulty == 'easy':
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS


def game():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    answer = random.randrange(1, 101)
    #print(answer)

    attempts = choose_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the hidden number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print("You ran out of guesses. You lost.")
            return
        elif guess != answer:
            print("Try again!")


game()
