# Built-in data types, operators, functions, and generators


# Factorial
# The factorial of the number N is the product of all integers 
# from 1 to N inclusive. 
# For example, the factorial of the number 5 is the product 
# of the numbers 1, 2, 3, 4, 5.

# The function should return the factorial of the argument, the number n.
def fac(n):
    f = 1
    i = 1
    while n >= i:
        f *= i
        i += 1
    return f

# The greatest common divisor (GCD) for two integers.

# We assume that both arguments are positive numbers. 
# One of the easiest ways to calculate the GCD is the Euclidean method,
# according to which

#     1. GCD(a, 0) = a
#     2. GCD(a, b) = GCD(b, a mod b)

#     (mod - operation to take the remainder of division, in python - the operator '%')
def gcd(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        while a !=0 and b !=0:
            if a>b:
                a = a%b
            else:
                b = b%a
    return a+b

# Generator for series  Fibonacci numbers

# You need to generate an infinite series of Fibonacci numbers, 
# in which each subsequent element of the series is the sum of the previous two. 
# Beginning of the sequence: 1, 1, 2, 3, 5, 8, 13, ..


def fgib():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b


def fib(n):
  f1 = 1
  f2 = 1
  i = 0
  while i < n - 2:
    fs = f1 + f2
    f1 = f2
    f2 = fs
    i += 1
  return f2


#  A function that converts nested objects of any nesting 
# level to a flat one-level one.

def flatten(seq):
    list_new=[]
    for x in seq:
        if type(x)!=list and type(x)!=tuple:
            list_new.append(x)
        else:
            list_new.extend(flatten(x))
    return list_new
    


