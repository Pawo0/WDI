def count_e(n):
    eps = 0.1 ** n
    i, e, fact, check_e = 2, 1, 1, 0
    while abs(check_e-e) > eps:
        check_e = e
        e += 1/fact
        fact *= i
        i += 1
    return e

print(count_e(100))