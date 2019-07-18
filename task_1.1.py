x = int(input('write number: '))

def fac(x):
    f =1
    i=1
    while i<=x:
        f*=i
        i+=1
    print (f)

fac(x)