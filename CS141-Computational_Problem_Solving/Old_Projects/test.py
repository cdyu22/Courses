# Fill in the function mystery(a, b) for question 5 below
a = int(input("What is a? "))
b = int(input("What is b? "))


def mystery(a, b):
    count = 3
    for i in range(b):
        count += 1
    print(count)
mystery(a,b)
