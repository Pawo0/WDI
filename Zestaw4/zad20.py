def zad20(t: list) -> tuple:
    n = len(t)
    naj = 0
    maks = tuple
    for i in range(n):
        for j in range(n):
            pkt_wiezy1 = (j, i)
            suma_wiersz, suma_kolumna = 0, 0
            for x in range(j):
                suma_wiersz += t[i][x]
            for x in range(j+1, n):
                suma_wiersz += t[i][x]

            for y in range(i):
                suma_kolumna += t[y][j]
            for y in range(i+1,n):
                suma_kolumna += t[y][j]

            for k in range(n):
                for l in range(n):
                    pkt_wiezy2 = (l, k)
                    suma_wiersz2, suma_kolumna2 = 0, 0
                    if pkt_wiezy1 != pkt_wiezy2:
                        for x in range(l):
                            if x != j:
                                suma_wiersz2 += t[i][x]
                        for x in range(l + 1, n):
                            if x != j:
                                suma_wiersz2 += t[i][x]

                        for y in range(k):
                            if y != i:
                                suma_kolumna2 += t[y][j]
                        for y in range(k + 1, n):
                            if y != i:
                                suma_kolumna2 += t[y][j]
                        suma_szach = suma_wiersz + suma_kolumna + suma_wiersz2 + suma_kolumna2
                        if suma_szach > naj:
                            naj = suma_szach
                            maks = (pkt_wiezy1, pkt_wiezy2)

    return maks


def test_case1():
    tab1 = [
        [2, 3, 3, 5, 7, 8, 8, 9],
        [1, 2, 2, 2, 3, 4, 5, 6],
        [1, 1, 2, 2, 3, 3, 45, 5],
        [4, 44, 5, 6, 2, 8, 9, 9],
        [2, 4, 4, 5, 60, 7, 8, 9],
        [1, 1, 2, 2, 3, 3, 4, 5],
        [1, 1, 2, 2, 3, 3, 4, 5],
        [1, 1, 2, 2, 3, 3, 4, 5],
    ]
    for wiersz in tab1:
        print(wiersz)
    print(zad20(tab1))


def test_case2():
    tab1 = [[2, 3, 3, 5, 7],
            [1, 2, 2, 22, 3],
            [4, 33, 5, 6, 7],
            [2, 4, 4, 5, 6],
            [1, 1, 2, 2, 3]
            ]
    for wiersz in tab1:
        print(wiersz)
    print(zad20(tab1))


if __name__ == "__main__":
    test_case2()