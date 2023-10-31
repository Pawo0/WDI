n = int(input("Podaj liczbe naluralna: "))
suma = 0

i = 1
k = 0
while suma <= n:
    suma += i
    i += 2
    k += 1

print(k-1)