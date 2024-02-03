names = names_string.split(", ")
# The code above converts the input into an array seperating
# each name in the input by a comma and space.

import random
num_items = len(names)
position = random.randint(0, num_items - 1)
purchaser = names[position]
print(f"{purchaser} is going to buy the meal today!")