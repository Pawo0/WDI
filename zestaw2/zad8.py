def sum_fib(n):
    x, y = 1, 1
    suma = 0
    while suma < n:
        suma += x
        x, y = y, x+y
    x, y = 1, 1
    while suma >= n:
        if suma == n:
            return True
        suma -= x
        x, y = y, x+y
    return False

def zad8(n):
    n += 1
    while True:
        if sum_fib(n) == False:
            return n
        n += 1

if __name__ == "__main__":
    print(zad8(9))
    print(zad8(15))