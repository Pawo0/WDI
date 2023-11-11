from random import randint


def rand_tab(x: int = 10):
    tab = [[randint(1,100) for _ in range(x)] for _ in range(x)]
    return tab


def w_wierszu_same_parzyste_cyfry(t: list) -> bool:
    for wiersz in t:
        flag = True
        for liczba in wiersz:
            tmpflag = False
            while liczba > 0:
                if liczba % 2 == 0:
                    tmpflag = True
                liczba //= 10
            if not tmpflag:
                flag = False
        if flag:
            return True
    return False


if __name__ == "__main__":
    tab = rand_tab(5)
    for x in tab:
        print(x)
    print(w_wierszu_same_parzyste_cyfry(tab))
