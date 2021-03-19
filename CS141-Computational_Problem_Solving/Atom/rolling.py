import random


two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
eleven = 0
twelve = 0

for i in range(10000):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    if die1 == 7:
        die1 = 1
    if die2 == 7:
        die2 = 1
    throw = die1 + die2
    if throw == 2:
        two += 1
    elif throw ==3:
        three += 1
    elif throw ==4:
        four += 1
    elif throw ==5:
        five += 1
    elif throw ==6:
        six += 1
    elif throw == 7:
        seven += 1
    elif throw == 8:
        eight += 1
    elif throw == 9:
        nine += 1
    elif throw ==10:
        ten += 1
    elif throw ==11:
        eleven +=1
    elif throw == 12:
        twelve +=1

print('two: ', two/10000)
print('three: ',three/10000)
print('four: ', four/10000)
print(five/10000)
print(six/10000)
print(seven/10000)
print(eight/10000)
print(nine/10000)
print(ten/10000)
print(eleven/10000)
print(twelve/10000)
