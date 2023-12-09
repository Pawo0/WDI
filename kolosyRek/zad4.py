from math import log10, sqrt


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0 or x == 1:
        return False
    i = 5
    while i <= sqrt(x):
        if x % i == 0:
            return False
        i += 2
        if x % i == 0:
            return False
        i += 4
    return True


def int_len(x):
    return int(log10(x))+1


def divide(number,res="",parts=0,j=0):
    if number == 0:
        if is_prime(parts):
            print(res)
        return is_prime(parts)
    n = int_len(number)
    for i in range(n-1-j,-1,-1):
        cut = number//(10**i)
        if is_prime(cut):
            return divide(number%(10**i),res+"{"+str(cut)+"}", parts+1,0) or divide(number,res, parts, j + 1)
    return False


print(divide(231525))
