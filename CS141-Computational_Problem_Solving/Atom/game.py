import random

target = random.randint(1,10) #Inclusive
guess = int(input("Guess a number, 1 through 10! "))

if guess == target:
    print("You got it!")
else:
    print("Failure, Guess again!")
    guess2 = int(input("Guess a number! "))
    if guess2 == target:
        print("You got it!")
    else:
        print("Wrong again, target was", target)
