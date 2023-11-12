def zad19(t: list, x: int) -> int:
    n = len(t)
    cnt = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
            if i - 1 >= 0 and j + 2 < n and t[i][j] * t[i-1][j+2] == x:
                cnt += 1
            if i + 1 < n and j + 2 < n and t[i][j] * t[i+1][j+2] == x:
                cnt += 1
            if i + 2 < n and j + 1 < n and t[i][j] * t[i+2][j+1] == x:
                cnt += 1
            if i + 2 < n and j - 1 >= 0 and t[i][j] * t[i+2][j-1] == x:
                cnt += 1
            j += 1
        i += 1
    return cnt


if __name__ == "__main__":
    tab1 = [[2, 3, 3, 5, 7],
            [1, 2, 2, 2, 3],
            [4, 4, 5, 6, 7],
            [2, 4, 4, 5, 6],
            [1, 1, 2, 2, 3]
        ]
    tab2 = [[0, 5, 0, 5, 0],
            [5, 0, 0, 0, 5],
            [0, 0, 2, 0, 0],
            [5, 0, 0, 0, 5],
            [0, 5, 0, 5, 0]
        ]
    print(zad19(tab2,10))
