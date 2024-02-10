import random
#from replit import clear
import os
from day011_art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(player_score, dealer_score):
  if player_score == dealer_score:
    return "Draw"
  elif dealer_score == 0:
    return "Lose, dealer has Blackjack"
  elif player_score == 0:
    return "Win with a Blackjack"
  elif player_score > 21:
    return "You went over, you lose"
  elif dealer_score > 21:
    return "Dealer went over, you win"
  elif player_score > dealer_score:
    return "You win"
  else:
    return "You lose"

def play_game():
  print(logo)
  player_hand = []
  dealer_hand = []
  game_over = False
  
  for _ in range(2):
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())
  
  while not game_over:
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    print(f"  Your cards: {player_hand}, current score: {player_score}")
    print(f"  Dealer's first cards: {dealer_hand[0]}")
    
    if player_score == 0 or dealer_score == 0 or player_score > 21:
      game_over = True
    else:
      player_continue = input("Type 'y' to get another card, type 'n' to pass: ")
      if player_continue == 'y':
        player_hand.append(deal_card())
      else:
        game_over = True
  
  while dealer_score != 0 and dealer_score < 17:
    dealer_hand.append(deal_card())
    dealer_score = calculate_score(dealer_hand)
  
  print(f"  Your final hand: {player_hand}, final score: {player_score}")
  print(f"  Dealer final hand: {dealer_hand}, final score: {dealer_score}")
  print(compare(player_score, dealer_score))

while input("Do you want to play a game of Blackjack?  Type 'y' or 'n': ") == 'y':
  #clear()
  os.system('clear')
  play_game()