from random import randint


def rand_tab(x: int = 10):
    tab = [[randint(0,10) for _ in range(x)] for _ in range(x)]
    return tab


def suma_kolumn_i_wierszy(t: list) -> tuple:
    n = len(t)
    wiersze = [0] * n
    kolumny = [0] * n
    for i in range(n):
        sum_w = 0
        sum_k = 0
        for j in range(n):
            sum_w += t[i][j]
            sum_k += t[j][i]
        wiersze[i] = sum_w
        kolumny[i] = sum_k
    return wiersze, kolumny

def max_iloraz_k_i_w(kolumny: list , wiersze:list) -> tuple:
    maks_k = None
    min_w = None
    kordy_k, kordy_w = -1, -1
    i = 0
    while i < len(kolumny):
        if  maks_k is None or kolumny[i] > maks_k:
            maks_k = kolumny[i]
            kordy_k = i
        if min_w is None or wiersze[i] < min_w:
            min_w = wiersze[i]
            kordy_w = i
        i += 1
    return kordy_k, kordy_w


if __name__ == "__main__":
    tab = rand_tab(5)
    for x in tab:
        print(x)
    print("-"*30)
    k,w = suma_kolumn_i_wierszy(tab)
    print(k,"\n",w)
    print(max_iloraz_k_i_w(k,w))