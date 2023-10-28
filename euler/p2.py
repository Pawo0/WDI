def fib(n):
    x, y, result  = 1, 2, 0
    while x < n:
        if x % 2 == 0:
            result += x
        x, y = y, x+y
    return result

print(fib(4_000_000))