def max_czynnik(n):
    i = 2
    result = 0
    while n != 1:
        while n % i == 0:
            n //= i
            result = i
        i += 1
    return result


def rek(t, id, l):
    if max_czynnik(l) == 0:
        return 0

    m = max_czynnik(l)
    rek(t, id+m, t[id+m])


t = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
