def f(t: list) -> list:
    width = len(t)
    cnt = 1
    a, b = 0, width-1
    while a < b:
        for i in range(a, b):
            t[a][i] = cnt
            t[i][b] = cnt + b - a
            cnt += 1
        cnt += b - a
        for i in range(b, a, -1):
            t[b][i] = cnt
            t[i][a] = cnt + b - a
            cnt += 1
        cnt += b - a
        a += 1
        b -= 1
    if a == b:
        t[a][b] = cnt
    return t


def tworz_tabele(x: int = 10) -> list:
    tab = [0] * x
    for i in range(len(tab)):
        tab[i] = [0] * x
    return tab


if __name__ == "__main__":
    tab = tworz_tabele(10)
    tab = f(tab)
    for i in tab:
        print(i)