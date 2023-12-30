from math import sqrt


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0 or x == 1:
        return False
    i = 5
    while i < sqrt(x):
        if x % i == 0:
            return False
        i += 2
        if x % i == 0:
            return False
        i += 4
    return True


def komnaty(T):
    def rek(i,s,res=""):
        if i == len(T) - 1:
            print(res+str(T[i]+s))
            return is_prime(T[i] + s) and T[i]+s <= 100
        for j in range(s-6,s+1):
            if T[i] + j > 1 and T[i]+j <= 100 and is_prime(T[i]+j):
                if rek(i+1,s-j,res+str(T[i]+j)+","):
                    return True
        return False
    return rek(0,0)


print(komnaty([10,20,35]))
