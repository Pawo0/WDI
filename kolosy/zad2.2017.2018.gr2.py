def is_palindrome(x) -> bool:
    revers = 0
    x_copy = x
    while x_copy != 0:
        digit = x_copy % 10
        revers = revers*10 + digit
        x_copy //= 10
    return revers == x


def func(t):
    n = len(t)
    maks = 0
    for i in range(n-1):
        number = t[i]
        if number % 2 == 1:
            for j in range(i+1,n):
                if number % 2 == 0:
                    break
                number = number*10 + t[j]
                dl = j - i + 1
                if is_palindrome(number):
                    maks = max(maks,dl)
    return maks