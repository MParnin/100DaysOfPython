import random
from day014_game_data import data
from day014_art import logo, vs
import os

end_game = False
previous_dict = {}
selection = {}
competitor = {}
dict_a = {}
dict_b = {}
score = 0

def select_entries():
    return random.choice(data)

def compare_followers(selection, competitor):
  if selection['follower_count'] >= competitor['follower_count']:
    global score
    global previous_dict
    global end_game
    score += 1
    os.system('clear')
    print(f"You're right! Current score: {score}")
    previous_dict = selection
    return
    
  else:
    os.system('clear')
    print(logo)
    print(f"Sorry, that's wrong.  Final score: {score}")
    end_game = True
  

def game():
  while end_game == False:
    print(logo)
    if not previous_dict:
      dict_a = select_entries()
      dict_b = select_entries()
    else:
      dict_a = previous_dict
      dict_b = select_entries()
    print(f"Compare A: {dict_a['name']},  {dict_a['description']},  {dict_a['country']}")
    print(vs)
    print(f"Compare B: {dict_b['name']},  {dict_b['description']},  {dict_b['country']}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    if user_choice == 'A':
      selection = dict_a
      competitor = dict_b
    else:
      selection = dict_b
      competitor = dict_a
    compare_followers(selection, competitor)

game()