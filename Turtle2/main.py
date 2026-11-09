from turtle import Turtle, Screen
import random

tartaruga = Turtle()
tartaruga.shape("turtle")
tartaruga.color("black")

# for _ in range(4):
#     tartaruga.right(90)
#     tartaruga.forward(100)

# for _ in range (10):
#     tartaruga.forward(10)
#     tartaruga.penup()
#     tartaruga.forward(10)
#     tartaruga.pendown()
colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "aquamarine", "orange", "purple", "blue violet"]

def draw_shapes(numb_of_sides):
    angle = 360 / numb_of_sides
    for _ in range(numb_of_sides):
        tartaruga.forward(100)
        tartaruga.right(angle)

for shape_side_number in range(3, 11):
    tartaruga.color(random.choice(colors))
    draw_shapes(shape_side_number)


schermo = Screen()
schermo.exitonclick()
