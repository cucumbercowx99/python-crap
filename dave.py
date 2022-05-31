import turtle
import random

dave = turtle.Turtle()
dave.shape("turtle")

dave.goto(0,0)
dave.pendown()

location = (random.randint(1,4))

if location == "1":
    dave.forward(random.randint(1,150))

if location == "2":
    dave.left(180)
    dave.forward(random.randint(1,150))

if location == "3":
    dave.left(90)
    dave.forward(random.randint(1,150))

if location == "4":
    dave.right(90)
    dave.forward(random.randint(1,150))

