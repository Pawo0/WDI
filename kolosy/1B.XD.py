def sudoku(t):
    for i in range(1,9):
        for j in range(i,10):
            zamien(t,i,j)
            if spr(t):
                return i, j
            zamien(t,i,j)


def zamien(tab,x,y):
    x1 = 2 + ((x-1) // 3) * 3
    x2 = 2 + ((x-1) % 3) * 3
    y1 = 2 + ((y-1) // 3) * 3
    y2 = 2 + ((y-1) % 3) * 3
    for i in range(3):
        for j in range(3):
            tab[x1-i][x2-j], tab[y1-i][y2-j] = tab[y1-i][y2-j], tab[x1-i][x2-j]


def spr(t):
    n = len(t)
    for i in range(n):
        tab_t = [1 for _ in range(10)]
        tab_t[0] = 0
        for j in range(n):
            tab_t[t[i][j]] = 0
        if sum(tab_t) > 0:
            return False
    for i in range(n):
        tab_t = [1 for _ in range(10)]
        tab_t[0] = 0
        for j in range(n):
            tab_t[t[j][i]] = 0
        if sum(tab_t) > 0:
            return False
    return True


t = [[8,1,2,7,5,3,6,4,9],
     [9,4,3,6,8,2,1,7,5],
     [6,7,5,4,9,1,2,8,3],
     [1,5,4,3,6,8,8,9,6],
     [3,6,9,9,1,7,7,2,1],
     [2,8,7,4,5,2,5,3,4],
     [5,2,1,9,7,4,2,3,7],
     [4,3,8,5,2,6,8,4,5],
     [7,9,6,3,1,8,1,6,9]]


print(sudoku(t))
