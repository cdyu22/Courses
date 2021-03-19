import turtle
#turtle() is the library of functions. It's a class, but we'll talk about that soon.
bob = turtle.Turtle()
bob.pencolor('Purple')
bob.pensize(5)

def drawSquare(tortoise,length):
    i=0
    while i<4:
        tortoise.forward(length)
        tortoise.right(90)
        i+=1


def drawRectangle(tortoise,length,width):
    for i in range(2):
        tortoise.forward(length)
        tortoise.right(90)
        tortoise.forward(width)
        tortoise.right(90)

def drawEquiTriangle(tortoise,length):
    for i in range(3):
        tortoise.right(120)
        tortoise.forward(length)

def drawPolygon(tortoise,side_length,num_sides):
    angle = 360/num_sides
    for i in range(num_sides):
        tortoise.forward(side_length)
        tortoise.right(angle)




bob.clear()#Stops all previous drawings
#turtle.done() Stops program
