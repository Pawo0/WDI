from math import pi

def silnia(x):
    if x == 0:
        return 1
    else:
        return silnia(x-1)*x


def licz_cos(x):
    cos, cos_check, znak, liczba, sil = 1, 0, -1, 1, 2
    EPS = 1e-100
    while abs(cos_check-cos) > EPS:
        liczba *= x*x
        cos_check = cos
        cos += (liczba/silnia(sil)*znak)
        znak *= -1
        sil += 2

    return cos


print(licz_cos(pi/3))
print(licz_cos(pi/4))
print(licz_cos(pi/6))