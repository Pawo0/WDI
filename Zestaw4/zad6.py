# beznadziejnie zrobione, sortowanie na koniec t2
def sort_babel_bez_0(t1: list):
    i = 0
    if min(t1) != 0:
        x = len(t1)
    else:
        x = [i for i in range(len(t1)) if t1[i] == 0]
        x = min(x)
    while i < x - 1:
        j = 0
        while j < x - i - 1:
            if t1[j] > t1[j+1]:
                t1[j], t1[j+1] = t1[j+1], t1[j]
            j += 1
        i += 1


def uzup_t2_singletonami(t1: list, t2: list):
    n = len(t1)
    j = 0
    for wiersz in t1:
        if wiersz[1] > wiersz[0]:
            t2[j] = wiersz[0]
            j += 1
        for i in range(1,n-1):
            if wiersz[i - 1] < wiersz[i] < wiersz[i + 1]:
                t2[j] = wiersz[i]
                j += 1
        if wiersz[-1] > wiersz[-2]:
            t2[j] = wiersz[-1]
            j += 1
    return t2


if __name__ == "__main__":
    tab1 = [[2, 3, 3, 5, 7], [1, 2, 2, 2, 3], [4, 4, 5, 6, 7], [2, 4, 4, 5, 6], [1, 1, 2, 2, 3]]
    tab2 = [0] * len(tab1) * len(tab1)
    result = uzup_t2_singletonami(tab1, tab2)
    print(result)
    sort_babel_bez_0(result)
    print(result)
