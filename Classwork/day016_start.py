# import turtle

# timmy = turtle.Turtle()
# print(timmy)
# timmy.fillcolor("DarkOrchid")
# timmy.shape("turtle")
# timmy.forward(100)

# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Charizard", "Blastoise", "Venusaur"]) 
table.add_column("Type", ["Fire", "Water", "Grass"])
table.align = "l"
print(table)

