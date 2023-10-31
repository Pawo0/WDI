def sum_podzielniki(x):
    i = 1
    suma = 0
    while i <= x/2:
        if x % i == 0:
            suma += i
        i += 1
    return suma


print(sum_podzielniki(220))