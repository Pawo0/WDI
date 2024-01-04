def czy_podciag_fib(x,y,z) -> bool:
    if x < z and x + y == z:
        while y > 1:
            x, y, z = y-x, x, y
        if x == y == 1 and z == 2:
            return True
        return False
    elif z < x and y + z == x:
        while y > 1:
            z, y ,x = y-z, z, y
        if y == z == 1 and x == 2:
            return True
        return False
    return False


def zad(T):
    n = len(T)
    for i in range(n-3):
        for j in range(n-3):
            if czy_podciag_fib(T[i][j],T[i+1][j],T[i+2][j]):
                k = 2
                cnt = 3
                while True:
                    if czy_podciag_fib(T[i+k-1][j],T[i+k][j],T[i+k+1][j]):
                        cnt += 1
                    else:
                        return cnt
                    k += 1

            if czy_podciag_fib(T[i][j],T[i][j+1],T[i][j+2]):
                k = 2
                cnt = 3
                while True:
                    if czy_podciag_fib(T[i][j+k-1],T[i][j+k],T[i][j+k+1]):
                        cnt += 1
                    else:
                        return cnt
                    k += 1
    return False

t = [
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 4, 0, 0, 0],
  [0, 0, 21, 0, 0, 0, 0, 0],
  [0, 0, 13, 0, 0, 0, 0, 0],
  [0, 0, 8, 0, 0, 0, 0, 0],
  [0, 0, 5, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0]
]
print(zad(t))