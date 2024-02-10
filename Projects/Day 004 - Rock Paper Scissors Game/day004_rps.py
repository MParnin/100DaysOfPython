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

import random

user_input = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

user_index = int(user_input)

if user_input == "0":
  print(rock)
elif user_input == "1":
  print(paper)
else:
  print(scissors)

print("Computer chose:")

computer_decision = random.randint(0, 2)

computer_index = computer_decision

if computer_decision == 0:
  print(rock)
elif computer_decision == 1: 
  print(paper)
else:
  print(scissors)

user_rock = ["It's a draw", "You lose", "You win"]
user_paper = ["You win", "It's a draw", "You lose"]
user_scissors = ["You lose", "You win", "It's a draw"]
decision_matrix = [user_rock, user_paper, user_scissors]
decision = decision_matrix[user_index][computer_index]

print(decision)