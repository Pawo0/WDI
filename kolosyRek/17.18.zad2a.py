def is_prime(n):
    if n == 2 or n == 3:
        return 1
    if n == 0 or n % 2 == 0 or n % 3 == 0 or n == 1:
        return 0
    i = 5
    while i <= int(n**0.5):
        if n % i == 0:
            return 0
        i += 2
        if n % i == 0:
            return 0
        i += 4
    return 1


def rek(t, i,used=[], fr=1, last=0):
    if i == 9:
        print(t)
        return 1
    for j in range(fr, 10):
        if (last == 0 or abs(last - j) >= 2) and j not in used:
            if is_prime(last) == is_prime(j) == 1:
                rek(t, i,used, fr + 1, last)
            else:
                t[i] = j
                rek(t, i + 1,used+[j], 1, j)
                t[i] = 0
        else:
            rek(t, i,used, fr + 1, last)
    return 0


t = [0 for i in range(9)]
rek(t,0)
