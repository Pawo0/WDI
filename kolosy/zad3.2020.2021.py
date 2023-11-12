# cos jest zle xd

def sum_row(t, row) -> int:
    suma = 0
    n = len(t)
    for i in range(n):
        suma += t[row][i]
    return suma


def sum_col(t, col) -> int:
    suma = 0
    n = len(t)
    for i in range(n):
        suma += t[i][col]
    return suma


def chess(t: list):
    n = len(t)
    result = ()
    maks = 0
    for row1 in range(n):
        for col1 in range(n):
            for row2 in range(n):
                for col2 in range(n):
                    if (row1, col1) != (row2, col2):
                        suma = (sum_row(t,row1) + sum_row(t,row2) + sum_col(t,col1) + sum_col(t,col2)
                                - 2*t[row1][col1] - 2*t[row2][col2] - t[row1][col2] - t[row2][col1])
                        if suma > maks:
                            result = (row1, col1, row2, col2)
                            maks = suma
    return (result, maks)

print(chess([[4,0,2],[3,0,0],[6,5,3]]))

print(chess([[1,1,2,3],
             [-1,3,-1,4],
             [4,1,5,4],
             [5,0,3,6]]))

