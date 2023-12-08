from math import sqrt


def is_complex(x):
    if x == 2 or x == 3:
        return 0
    if x % 2 == 0 or x % 3 == 0:
        return 1
    i = 5
    while i <= sqrt(x):
        if x % i == 0:
            return 1
        i += 2
        if x % i == 0:
            return 1
        i += 4
    return 0


def zad26b(a,b):
    def rek(a,b,res):
        if a == b == 0:
            return is_complex(res)
        x, y = 0, 0
        if a > 0:
            x = rek(a - 1, b, res + 2 ** (a + b - 1))
        if b > 0:
            y = rek(a, b - 1, res + 2 ** (a + b - 1))
        return x + y

    return (a-1,b,2**(a+b-1))




def zad26(a,b):
    a -= 1
    def rek(a,b,res=1):
        if a == b == 0:
            print(res)
        else:
            if a > 0:
                rek(a-1,b,res*10+1)
            if b > 0:
                rek(a,b-1,res*10)
    rek(a,b)

zad26(2,3)