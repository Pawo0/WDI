import math

def sum_podzielniki(x):
    i = 2
    suma = 1
    while i <= math.sqrt(x):
        if x % i == 0:
            suma += i
            if i != x//i :
                suma += x//i
        i += 1
    return suma

def czy_zaprz(x):
    y = sum_podzielniki(x)
    if sum_podzielniki(y) == x and x < y:
        return print(x,y)
    else:
        return False

for i in range(1,1000000):
    if czy_zaprz(i):
        pass