def fib(szukana):
    a, b = 1, 1
    while True:
        if szukana == a*b:
            return True
        elif szukana < a*b:
            return False
        a, b = b, a+b

x = int(input("Podaj liczbe: "))

print(fib(x))