
def triangle():
    levels = int(input("How many levels should there be? \nEnter an Odd Number:"))
    if levels%2 != 1:
        triangle()
    direction(levels)

def direction(levels):
    direction = int(input("Where would you like the triangle to point? \n 1) down \n 2) up \n 3) left \n 4) right \n Please Select a Number: "))
    if direction == 1:
        space=0
        while levels != 0:
            stars= 1+2*(levels-1)
            print(" "*space+"*"*stars)
            levels = levels-1
            space+=1
    elif direction == 2:
        x = levels
        while levels != 0:
            stars = 1+2*(x-levels)
            print(" "*levels,"*"*stars)
            levels = levels-1
    elif direction == 3:
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
    elif direction == 4:
        x=1
        while levels > x:
            print("*"*x)
            x=x+1
        while 0 < x <= levels:
            print("*"*x)
            x=x-1
    else:
        direction = int(input("Where would you like the triangle to point? \n 1) down \n 2) up \n 3) left \n 4) right \n Please Select a Number: "))
        direction()


triangle()
