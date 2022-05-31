import turtle
import random

derek = turtle.Turtle()

direction = random.randint(1,4)

derek.goto(0,0)

for i in range (500):
    if direction == 1:
        derek.forward(random.randint(1,250))
    elif direction == 2:
        derek.right(90)
        derek.forward(random.randint(1,250))
    elif direction == 3:
        derek.right(180)
        derek.forward(random.randint(1,250))
    elif direction == 4:
        derek.right(270)
        derek.forward(random.randint(1,250))
