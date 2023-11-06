def zad9(t: list, k: int) -> tuple:
    n = len(t)
    wynik = tuple

    for bok in range(2, n, 2):
        for start_y in range(0, n - bok):
            for start_x in range(0,n-bok):
                a = t[start_y][start_x]
                b = t[start_y][start_x+bok]
                c = t[start_y+ bok][start_x+bok]
                d = t[start_y+ bok][start_x]
                if a * b * c * d == k:
                    print(f"S = ({int(start_x+bok/2)} {int(start_y+bok/2)}) o boku {bok+1}")



def test_case1():
    tab1 = [
        [2, 3, 3, 5, 7, 8, 8, 9],
        [1, 2, 2, 2, 3, 4, 5, 6],
        [1, 1, 2, 2, 3, 3, 4, 5],
        [4, 4, 5, 6, 2, 8, 9, 9],
        [2, 4, 4, 5, 6, 7, 8, 9],
        [1, 1, 2, 2, 3, 3, 4, 5],
        [1, 1, 2, 2, 3, 3, 4, 5],
        [1, 1, 2, 2, 3, 3, 4, 5],
    ]
    for wiersz in tab1:
        print(wiersz)
    zad9(tab1, 60)


def test_case2():
    tab2 = [[2, 3, 3, 5, 7],
            [1, 2, 2, 2, 3],
            [4, 4, 5, 6, 7],
            [2, 4, 4, 5, 6],
            [1, 1, 2, 2, 3]
            ]
    for wiersz in tab2:
        print(wiersz)
    zad9(tab2, 360)


if __name__ == "__main__":
    test_case2()

