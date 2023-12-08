
def zad31(t):
    n = len(t)
    result = 0
    def rek(j=0, ilo=1):
        nonlocal n, result
        if j == n:
            result += ilo
        else:
            rek(j+1,ilo*t[j])
            rek(j+1,ilo)
    rek()
    return result - 1


t = [2,3,5]

print(zad31(t))