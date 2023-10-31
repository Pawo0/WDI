from math import sqrt

def czy_pierwsza(x):
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True

print(czy_pierwsza(82))
print(czy_pierwsza(83))
