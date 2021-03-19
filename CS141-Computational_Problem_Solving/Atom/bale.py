import turtle
import random
import math

class Bale:

    def __init__(self,childcolor):
        self.__food = turtle.Turtle(visible = False)
        self.__food.penup()
        self.__food.color('green')
        self.__food.goto(random.randint(-200,200),random.randint(-200,200))
        self.__food.showturtle()

        self.__parent1 = turtle.Turtle(visible = False)
        self.__parent1.penup()
        self.__parent1.color('purple')
        self.__parent1.goto(random.randint(-100,100),random.randint(-100,100))
        self.__parent1.showturtle()

        self.__parent2 = turtle.Turtle(visible = False)
        self.__parent2.penup()
        self.__parent2.color('purple')
        self.__parent2.goto(random.randint(-100,100),random.randint(-100,100))
        self.__parent2.showturtle()

        self.__child = turtle.Turtle(visible = False)
        self.__child.penup()
        self.__child.color('childcolor')
        self.__child.goto(random.randint(-100,100),random.randint(-100,100))
        self.__child.showturtle()

    def move(self):
        direction = random.randint(0,3)
        self.__food.right(90 * direction)
        self.__food.forward(10)
        fx = self.__food.xcor()
        fy = self.__food.ycor()
        p1x = self.__parent1.xcor()
        p1y = self.__parent1.ycor()
        parent1angle = self.__parent1.towards(fx,fy)
        self.__parent1.setheading(0)
        self.__parent1.left(parent1angle)
        self.__parent1.forward(20)

        p2x = self.__parent2.xcor()
        p2y = self.__parent2.ycor()

        xdiff = fx - p2x
        ydiff = fy - p2y
        parent2angle = math.degrees(math.atan(ydiff/xdiff))

        if xdiff > 0 and ydiff > 0:
            self.__parent2.setheading(0)
            self.__parent2.left(parent2angle)
        elif ydiff <0 and xdiff > 0:
            self.__parent2.setheading(0)
            self.__parent2.right(-parent2angle)
        elif ydiff > 0 and xdiff < 0:
            self.__parent2.setheading(180)
            self.__parent2.right(-parent2angle)
        elif ydiff < 0 and xdiff < 0:
            self.__parent2.setheading(180)
            self.__parent2.left(parent2angle)

        self.__parent2.forward(20)

        distance1 = self.__child.distance(p1x,p1y)
        distance2 = self.__child.distance(p2x,p2y)
        if distance1 <= distance2:
            childangle = self.__child.towards(p1x,p1y)

        else:
            childangle = self.__child.towards(p2x,p2y)
        self.__child.setheading(0)
        self.__child.left(childangle)
        self.__child.forward(15)


family = Bale('black')
family2 = Bale('blue')
for i in range(20):
    family.move()
    family2.move()

turtle.done()
