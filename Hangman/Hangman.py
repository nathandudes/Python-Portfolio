import random
import Hangman_words
import Hangman_art

print(Hangman_art.logo)
chosen_word = random.choice(Hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Creates "_"
display = []
for _ in range(word_length):
    display += "_"

# RUNS THE GAME
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter.upper()

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"'{guess.upper()}' is an incorrect guess. (-1 life)")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(Hangman_art.stages[lives])
