def product(a,b,c):
    a = (a*b*c)/3
    return a

def double_quotient(n,d):
    b=2*(n/d)
    return b

def square_sum(e,f):
    c=(e+f)**2
    return c

double_quotient(square_sum(product(6,4,5),29),3)

print((double_quotient(square_sum(product(6,4,5),29),3))*(product(double_quotient(28,4),square_sum(product(4,5,9),product(27,5,1)),6)))
