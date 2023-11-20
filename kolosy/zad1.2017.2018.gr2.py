def czy_sum_z_fib(n):
    x = 1
    y = 1
    sum = 0
    while sum < n:
        sum += x
        x, y = y, x+y
    x, y = 1, 1
    while sum > n:
        sum -= x
        x, y = y, x+y
    return sum == n


def func(n):
    i = n + 1
    while czy_sum_z_fib(i):
        i += 1
    return i

print(func(14))