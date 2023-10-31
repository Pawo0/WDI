# def sum_podzielniki(x):
#     i = 1
#     suma = 0
#     while i <= x/2:
#         if x % i == 0:
#             suma += i
#         i += 1
#     return suma
#
# def doskonale(x):
#     if x == sum_podzielniki(x):
#         return True
#     else:
#         return False

def czy_doskonala(x):
    suma = sum([i for i in range(1, int(x/2+1)) if x % i == 0])
    return suma == x

for i in range(1, 1000001):
    if czy_doskonala(i):
        print(i)