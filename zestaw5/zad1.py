from math import sqrt, log10


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


def len_int(n):
    return int(log10(n))+1


def wytnij(n,i):
    reszta = n % 10 ** (i - 1)
    przed = n // 10 ** i
    return przed * 10**(i-1) + reszta


def rec(num,i=1):
    if len_int(num) == 1 or len_int(num) < i:
        if is_prime(num):
            print(num)
        return
    rec(num, i + 1)
    rec(wytnij(num,i),i)

rec(311)