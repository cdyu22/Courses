# Fill in the function mystery(a, b) for question 5 below
a = int(input("What is a? "))
b = int(input("What is b? "))


def mystery(a, b):
    a = a%10
    b = b%10
    y = a
    z = b
    c = b
    b = (a + b)%10
    a = c
    count = 3
    while((a != y) or (b != z)):
        c = b
        b = (a + b)%10
        a = c
        count = count + 1
    print(count)
mystery(a,b)
