from math import sqrt

def czy_bez_powtorki(x) -> bool:
    x = int(x)
    liczby = ""
    while x != 0:
        liczba = str(x % 10)
        x //= 10
        if liczba in liczby:
            return False
        else:
            liczby += liczba
    return True


def pierwsza(x):
    x = int(x)
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


def func(liczba):
    liczba = str(liczba)
    najw = 0
    n = len(liczba)
    for i in range(n):
        for j in range(n,i,-1):
            if czy_bez_powtorki(liczba[i:j]) and pierwsza(liczba[i:j]):
                najw = max(najw, int(liczba[i:j]))
    return najw


print(func(102742516))