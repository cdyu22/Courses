import random

target = random.randint(1,1000)
guess = int(input("Guess a number between 1 and 1000 (0 for exit): "))

while target != guess and guess != 0:
    if target >guess:
        print('Guess a Larger Number')
    else:
        print('Guess a Smaller Number')
    guess = int(input("Guess again: "))


if guess != 0:
    print('YOU GOT IT')
