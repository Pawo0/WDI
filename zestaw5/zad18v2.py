from math import log10


def int_len(n):
    return int(log10(n)) + 1


def king(t,w=0,k=0):
    if w == k == len(t)-1:
        return True
    flag = False
    moves = ((1, 1), (1, 0), (0, 1))
    for x, y in moves:
        next_p = (w+x, k+y)
        if next_p[0] < len(t) and next_p[1] < len(t):
            next_val = t[next_p[0]][next_p[1]]
            var1 = t[w][k] % 10
            var2 = next_val // 10 ** (int_len(next_val)-1)
            if var1 < var2:
                flag = flag or king(t, next_p[0], next_p[1])
    return flag


t2 = [[1, 6, 62, 13, 18, 1, 8, 8],
      [8, 23, 62, 13, 3, 19, 5, 1],
      [15, 20, 10, 41, 7, 92, 32, 5],
      [17, 3, 11, 1, 7, 32, 3, 13],
      [14, 4, 14, 1, 6, 8, 42, 2],
      [16, 19, 12, 1, 11, 91, 4, 18],
      [13, 17, 15, 12, 2, 17, 51, 8],
      [8, 13, 18, 1, 8, 75, 57, 9]]

print(king(t2))