def waga(num):
    i = 2
    cnt = 0
    while num != 1:
        if num % i == 0:
            cnt += 1
        while num%i == 0:
            num //= i
        i += 1
    return cnt


def zad2(T):
    n = len(T)

    def rec(i=0,a=0,b=0,c=0):
        if i == n:
            return a == b and b == c
        return rec(i+1, a+waga(T[i]), b, c) or rec(i+1, a, b + waga(T[i]), c) or rec(i+1, a, b, c + waga(T[i]))

    return rec()


tab = [2,64,1,32]
print(zad2(tab))