def ciag_g(x: list) -> int:
    r = x[1] / x[0]
    ctn, max_ctn, i = 1, 1, 1
    while i < len(x):
        if x[i] / x[i-1] == r:
            ctn += 1
        else:
            max_ctn = max(ctn, max_ctn)
            r = x[i] / x[i-1]
            ctn = 2
        i += 1
    return max(ctn, max_ctn)


def zad8(t: list) -> tuple:
    n = len(t)
    najdl = 0
    for i in range(n-2):
        ciag = [0] * (n-i)
        for j in range(n-i):
            # po osi X
            ciag[j] = t[j][i + j]
        dl = ciag_g(ciag)
        if dl > najdl:
            najdl = dl

        ciag = [0] * (n - i)
        for j in range(n-i):
            # po osi Y
            ciag[j] = t[i + j][j]
        dl = ciag_g(ciag)
        if dl > najdl:
            najdl = dl
    if najdl < 3:
        return False, 0
    else:
        return True, najdl


if __name__ == "__main__":
    tab1 = [[2, 3, 3, 5, 7], [1, 4, 9, 2, 3], [4, 4, 8, 6, 7], [2, 4, 5, 5, 6], [1, 1, 2, 2, 3]]
    for wiersz in tab1:
        print(wiersz)
    print("*"*30)
    flag, dl = zad8(tab1)
    if flag:
        print(dl)
