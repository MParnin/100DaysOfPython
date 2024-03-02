# from colorgram import extract
# rgb_colors = []
# colors = extract("./Projects/Day 018 - Hirst Painting/image.png", 10)

# for color in colors:
#     r= color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle
import random


turtle.colormode(255)
screen = turtle.Screen()
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(206, 161, 84), (55, 88, 129), (142, 91, 41), (220, 207, 109), (139, 26, 49), (134, 175, 199)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_dots = 100


for dot_count in range(1, num_dots + 1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()



