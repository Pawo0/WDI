from random import randint


def rand_tab(x: int = 10):
    tab = [[randint(1,100) for _ in range(x)] for _ in range(x)]
    return tab


def w_kazdym_wierszu_nieparzyst(t: list) -> bool:
    for wiersz in t:
        flag = False
        for liczba in wiersz:
            tempflag = True
            while liczba > 0:
                if liczba % 2 == 0:
                    tempflag = False
                liczba //= 10
            if tempflag:
                flag = True
                break
        if not flag:
            return False
    return True


if __name__ == "__main__":
    tab = rand_tab(5)
    for x in tab:
        print(x)
    print(w_kazdym_wierszu_nieparzyst(tab))
