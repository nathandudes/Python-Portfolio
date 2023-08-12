import random
import HigherLower_art
import HigherLower_data

print(HigherLower_art.logo)
NAME = ''
DESCRIPTION = ''
COUNTRY = ''
FOLLOWERS = 0
FOLLOWERS_A = 0
FOLLOWERS_B = 0
SCORE = 0
GAME_OVER = False


def choosing_data():
    global NAME, DESCRIPTION, COUNTRY, FOLLOWERS
    for _ in HigherLower_data.data:
        random_data = random.choice(HigherLower_data.data)
        NAME = random_data['name']
        DESCRIPTION = random_data['description']
        COUNTRY = random_data['country']
        FOLLOWERS = random_data['follower_count']


def compare_a():
    global FOLLOWERS_A
    choosing_data()
    FOLLOWERS_A = FOLLOWERS
    print(f"Compare A: {NAME}, a {DESCRIPTION}, from {COUNTRY}.")


def compare_b():
    global FOLLOWERS_B
    choosing_data()
    FOLLOWERS_B = FOLLOWERS
    print(f"Against B: {NAME}, a {DESCRIPTION}, from {COUNTRY}.")


while not GAME_OVER:
    compare_a()
    print(HigherLower_art.vs)
    compare_b()
    answer = input("\nWho has more followers? Typer 'A' or 'B'").lower()

    if answer == "a" and FOLLOWERS_A > FOLLOWERS_B:
        SCORE += 1
        print(f"You're right! Current score: {SCORE}")
    elif answer == "b" and FOLLOWERS_B > FOLLOWERS_A:
        SCORE += 1
        print(f"You're right! Current score: {SCORE}")
    else:
        GAME_OVER = True
        print(f"Sorry, that's wrong. Final Score: {SCORE}")
