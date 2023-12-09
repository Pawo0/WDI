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

def zad5(t):
    n = len(t)
    def rek(p=0):
        if p == n:
            return True
        liczba = 0
        for i in range(p,n):
            liczba = liczba*2 + t[i]
            if is_prime(liczba):
                return rek(i+1)
        return False
    return rek()


t = [int(x) for x in "110100"]
print(zad5(t))

