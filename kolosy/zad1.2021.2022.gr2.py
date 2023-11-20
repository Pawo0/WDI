from math import sqrt


def pierwsza(x):
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


def func(t):
    n = len(t)
    ilo = 1
    index = -1
    for i in range(n):
        if pierwsza(t[i]):
            ilo *= t[i]
        elif ilo == t[i]:
            index = i
    return index if ilo > 1 else None


tab = [1,3,8,5,6,8,15,7,34]
print(func(tab))
