# Zawsze tworzy zadana tabele

from random import randint


def stworz_tabele(x: int=10) -> list:
    return [[randint(1, 100) for _ in range(x)] for _ in range(x)]

def zad10(t: list):
    n = len(t)
    for wiersz in t:
        flag = False
        for liczba in wiersz:
            while liczba != 0:
                if liczba % 10 == 0:
                    flag = True
                    break
                liczba //= 10
            if flag:
                break
        if not flag:
            return False
    i = 0
    while i < n:
        flag = False
        j = 0
        while j < n:
            liczba = t[j][i]
            while liczba != 0:
                if liczba % 10 == 0:
                    flag = True
                    break
                liczba //= 10
            if flag:
                break
            j += 1
        if not flag:
            return False
        i += 1
    return True


def do_skutku():
    flag = False
    while not flag:
        tab = stworz_tabele(5)
        flag = zad10(tab)
    for wiersz in tab:
        print(wiersz)


if __name__ == "__main__":
    do_skutku()