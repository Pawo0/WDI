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


if __name__ == "__main__":
    print(sum_fib(555))