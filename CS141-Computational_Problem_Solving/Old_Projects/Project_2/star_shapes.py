import sys

def rectangle():
    rwidth = int(input("How wide should the rectangle be? "))
    rheight = int(input("How high should the rectangle be? "))
    build_rectangle(rwidth,rheight)

def build_rectangle(rwidth,rheight):
    while rheight != 0:
        print("*"*rwidth)
        rheight=rheight-1


def direction(levels):
    directions = int(input("Where would you like the triangle to point? \n 1) down \n 2) up \n 3) left \n 4) right \n Please Select a Number: "))
    if directions == 1:
        down(levels)
    elif directions == 2:
        up(levels)
    elif directions == 3:
        left(levels)
    elif directions == 4:
        right(levels)
    else:
        direction(levels)

### Direction Functions
def down(levels):
    space=0
    while levels != 0:
        stars= 1+2*(levels-1)
        print(" "*space+"*"*stars)
        levels = levels-1
        space+=1

def up(levels):
    x = levels
    while levels != 0:
        stars = 1+2*(x-levels)
        print(" "*levels,"*"*stars)
        levels = levels-1

def left(levels):
    x = 1
    space = levels-1
    while levels > x:
        print(" "*space,"*"*x)
        x = x+1
        space = space-1
    while 0 < x <= levels:
        print(" "*space,"*"*x)
        x=x-1
        space = space+1

def right(levels):
    x=1
    while levels > x:
        print("*"*x)
        x=x+1
    while 0 < x <= levels:
        print("*"*x)
        x=x-1


def triangle():
    levels=int(input("Enter an Odd Number: "))
    if levels%2 != 1 or levels==2:
        triangle()
    else:
        direction(levels)

def octagon():
    length = int(input("How long should each side of the octagon be? "))
    build_octagon(length)

def build_octagon(length):
    stars = length
    side = length
    space = length-1
    while side >= 2:
        print(" "*space,"*"*stars)
        stars = stars+2
        side=side-1
        space = space-1
    while side != length:
        print(" "*space,"*"*stars)
        side = side+1
    while side >= 1:
        print(" "*space,"*"*stars)
        stars = stars-2
        side=side-1
        space= space+1

def function():
    print("This program can: \n 1) Draw a Rectangle. \n 2) Draw an Isoscles Triangle. \n 3) Draw an Octagon.")
    choice = int(input("Please Select a number or 0 to exit: "))
    if choice == 0:
        sys.exit()
    elif choice == 1:
        rectangle()
        function()
    elif choice == 2:
        print("How many levels should there be?")
        triangle()
        function()
    elif choice == 3:
        octagon()
        function()
    else:
        function()

function()
