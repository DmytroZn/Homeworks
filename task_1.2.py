a = int(input('write first number: '))
b = int(input('write second number: '))

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
    print(a+b)

gcd(a,b)