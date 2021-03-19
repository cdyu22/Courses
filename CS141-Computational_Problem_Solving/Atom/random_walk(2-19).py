import turtle
import random

bob = turtle.Turtle()
bob.speed(10)
for i in range(100):
    bob.forward(20)
    direction = random.randint(0,3)
    bob.right(90*direction)

#turtle.done()
