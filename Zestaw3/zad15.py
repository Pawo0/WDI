from math import sqrt
from random import randint


def fib(n: int) -> bool:
    if n == 1:
        return True
    x, y = 1, 1
    while x < n:
        x, y = y, x+y
        if x == n:
            return True
    return False


def prime_number(n: int):
    if n == 2 and n == 3:
        return True
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True



def zad15(t: list) -> bool:
    i = 0
    prime = False
    while i < len(t):
        if fib(i):
            if prime_number(t[i]):
                return False
        else:
            if prime_number(t[i]):
                prime = True
        i += 1
    return prime


if __name__ == "__main__":
    tab = [4,4,4,6,4,8,4,11,4]
    print(zad15(tab))
