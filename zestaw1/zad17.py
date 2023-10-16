EPS = 1e-8

def fib(x=1,y=1):
    iloraz = 0
    while abs(iloraz-x/y) > EPS:
        iloraz = x/y
        x, y = y, x+y
    return x/y

def zad17():
    print(fib())
    print(fib(4,10))
    print(fib(999,444))
    print(fib(12,4747))


if __name__ == "__main__":
    zad17()
