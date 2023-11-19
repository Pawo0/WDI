def len_number(x):
    if x == 0:
        return 1
    cnt = 0
    while x > 0:
        x //= 10
        cnt += 1
    return cnt


def a(x):
    if len_number(x) >= 2:
        last = x % 10
        x //= 10
        second = x % 10
        x //= 10
        return x * 100 + last * 10 + second
    return x


def b(x):
    return x*3


def c(x):
    length = len_number(x)
    if length >= 2:
        return x % pow(10, length-1)
    return x


def func(x,y):
    mask = [0,0,0,0,0,0,0]
    for i in range(1, pow(4,7)):
        x_mod = x
        j = 0
        while i != 0:
            mask[j] = i % 4
            i //= 4
            j += 1
        for operation in mask:
            if operation == 1:
                x_mod = a(x_mod)
            elif operation == 2:
                x_mod = b(x_mod)
            elif operation == 3:
                x_mod = c(x_mod)
        if x_mod == y:
            char = " ABC"
            result = ""
            for i in mask:
                result += char[i]
            return result
    return "ni mo"


print(func(6,3))
print(func(52,4))