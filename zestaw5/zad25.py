def czynniki_pierwsze(n):
    i = 2
    result = []
    while n != 1:
        if n % i == 0:
            result += [i]
        while n % i == 0:
            n //= i
        i += 1
    return result

def zad25(t):
    n = len(t)

    def rek(i=0,j=0):
        if i == n-1:
            return True
        else:
            czynniki = czynniki_pierwsze(t[i])
            for k in range(j, len(czynniki)):
                if i + czynniki[k] < n and czynniki[k] < t[i]:
                    return rek(i+czynniki[k], 0) or rek(i, k+1)
        return False
    return rek()


t = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
t1 = [10, 4, 2, 8, 10, 12, 14, 6, 18, 20, 3]

print(zad25(t1))
