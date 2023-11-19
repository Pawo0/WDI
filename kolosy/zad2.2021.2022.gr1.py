# trza kombinowac z maska bitowa xd

def na_czwork(x):
    result = ""
    while x != 0:
        digit = x % 4
        result = str(digit) + result
        x //= 4
    return int(result)


def ktore_liczby_wystepuja(t):
    n = len(t)
    digits = [[0]*4 for _ in range(n)]
    for i in range(n):
        x = na_czwork(t[i])
        while x != 0:
            digit = x % 10
            digits[i][digit] = 1
            x //= 10
    return digits


def func(t):
    pass