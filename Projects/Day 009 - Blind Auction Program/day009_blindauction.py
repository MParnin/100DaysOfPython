#from replit import clear
import os
from day009_art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

bids = {}

def auction_input():
  name = input("What is your name?\n")
  price = int(input("What is your bid?\n$ "))
  bids[name] = price

auction_input()

repeat = True

while repeat == True:
  
  more_bidders = input("Are there any other users who want to bid? Yes/No\n")
  
  if more_bidders == "yes":
    #clear()
    os.system('clear')
    auction_input()
  
  else:
    repeat = False
    print(f"{max(bids, key=bids.get)} is the winner")