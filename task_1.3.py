# два варіанти 
'''
#1)
x=int(input())  #використовую формулу для розрахунку https://geleot.ru/education/math/analytic_geometry/other/Fibonacci_number
def fib(x):
  a=(((1+5**(1/2)))/2)**x
  b=(((1-5**(1/2)))/2)**x
  c= 5**(1/2)
  return int((a-b)/c)
print(fib(x))
'''

#2)
x = int(input())
 
def fib(x):
  f1 = 1
  f2 = 1
  i = 0
  while i < x - 2:
    fs = f1 + f2
    f1 = f2
    f2 = fs
    i += 1
  return f2
 
print(fib(x))
