from turtle import Turtle, Screen
from random import randrange, randint

tim = Turtle()
tim.shape("turtle")
tim.color("DarkOliveGreen4")
screen = Screen()
screen.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color

### Turtle Challenge 1: Square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

### Turtle Challenge 2: Dashed Line
# for _ in range(50):
#     tim.forward(5)
#     tim.up()
#     tim.forward(5)
#     tim.down()

### Turtle Challenge 3: Different Shapes
# sides = 3
# for _ in range(3,11):
#     angle = 360 / sides
#     tim.pencolor((randrange(0,256), randrange(0,256), randrange(0,256)))
#     for side in range(sides):
#         tim.forward(50)
#         tim.right(angle)
#     sides += 1

### Turtle Challenge 4: Random Walk
##TO-DO:
## - [x] Thicker line
## - [x] Random colors
## - [x] Choose direction randomly: list of dictionaries
# tim.pensize(width=20)
# tim.speed(5)

# def direction():
#     value = randrange(0, 5)
#     angle = value * 90
#     return angle

# for _ in range(1000):
#     tim.pencolor((randrange(0,256), randrange(0,256), randrange(0,256)))
#     tim.forward(50)
#     tim.right(direction())

### Turtle Challenge 5: Spirograph
##TO-DO:
## - [x] radius = 100
## - [x] Random colors
## - [x] Draw a circle
## - [x] Change tilt
tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen.exitonclick()