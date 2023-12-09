def prime_factors(n):
    tab = []
    i = 2
    while n != 1:
        if n % i == 0:
            tab += [i]
        while n % i == 0:
            n //= i
        i += 1
    return tab


def zad22(t):
    n = len(t)
    result = -1

    def rek(i=0,jumps=0):
        nonlocal result
        if i == n-1:
            return jumps
        factors = prime_factors(t[i])
        for f in factors:
            if i+f < n and f < t[i]:
                result = max(rek(i+f,jumps+1),result)
        return result
    rek()
    return result


t = [10, 4, 2, 8, 10, 12, 14, 6, 18, 20, 3]  # 3
t2 = [10, 4, 2, 8, 10, 12, 14, 6, 18, 20, 3, 5]  # 4
print(zad22(t))
