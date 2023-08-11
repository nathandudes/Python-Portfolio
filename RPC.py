import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

print("WELCOME TO ROCK PAPER SCISSORS!")
player_choice = input("Choose wisely...\nType '0' for Rock, '1' for Paper, and '2' for Scissors.\n")
options = ["0", "1", "2"]
computer_choice = random.choice(options)


if player_choice == '0':
    print(f"You choose ROCK:\n{rock}")
elif player_choice == '1':
    print(f"You choose PAPER:\n{paper}")
elif player_choice == '2':
    print(f"You choose SCISSORS:\n{scissors}")
else:
    print("INVALID NUMBER. TRY AGAIN.")


if computer_choice == options[0]:
    print(f"Computer chose ROCK:\n{rock}")
elif computer_choice == options[1]:
    print(f"Computer chose PAPER:\n{paper}")
else:
    print(f"Computer chose SCISSORS:\n{scissors}")


if player_choice == '0' and computer_choice == options[2]:
    print("You Win!")
elif player_choice == '1' and computer_choice == options[0]:
    print("You Win!")
elif player_choice == '2' and computer_choice == options[1]:
    print("You Win!")
elif player_choice == computer_choice:
    print("TIE!")
else:
    print("You lose!")
