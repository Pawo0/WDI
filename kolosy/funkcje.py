from math import sqrt


def czy_pierwsza(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i <= sqrt(x):
        if x % i == 0:
            return False
        i += 2
        if x % i == 0:
            return False
        i += 4
    return True


def nwd(a,b):
    if b > 0:
        return nwd(b, a%b)
    return a


def dodawanie(x: list,y: list) -> list:
    r = 0
    i = len(x)
    result = [0 for _ in range(len(x))]
    while i >= 0:
        result[i] = (x[i]+y[i])%10+r
        r = (x[i]+y[i]) // 10
        i -= 1
    return result


def mnozenie(x: list, y: int) -> list:
    r = 0
    i = len(x)
    result = [0 for _ in range(i)]
    while i >= 0:
        result[i] = (x[i]*y) % 10 + r
        r = (x[i]*y) // 10
        i -= 1
    return result


def dzielenie(x,y,n):
    wynik = ""
    wynik += str(x // y) + "."
    for i in range(n+1):
        x = x % y * 10
        wynik += str(x // y)
    return wynik
