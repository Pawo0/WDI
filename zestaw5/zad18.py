from math import log10


def zad18(t,w=0,k=0):
    if w == k == len(t)-1:
        return True
    else:
        flag = False
        ruchy = [(1,1),(1,0),(0,1)]
        for ruch in ruchy:
            if ruch[0] + w < len(t) and ruch[1] + k < len(t):
                next_n = t[w + ruch[0]][k + ruch[1]]
                if t[w][k] % 10 < next_n // 10 ** (int(log10(next_n))):
                    flag = flag or zad18(t,w + ruch[0], k + ruch[1])
    return flag


t1 = [[17, 1, 9, 15, 10, 12, 19, 20],
     [10, 2, 16, 15, 12, 18, 19, 18],
     [18, 1, 17, 10, 14, 10, 6, 10],
     [5, 14, 3, 3, 8, 8, 20, 16],
     [19, 6, 14, 15, 17, 7, 13, 17],
     [16, 3, 18, 10, 5, 14, 16, 1],
     [13, 5, 16, 8, 18, 8, 18, 7],
     [7, 17, 6, 17, 8, 14, 14, 7]]


t2 = [[1, 6, 62, 13, 18, 1, 8, 8],
      [8, 23, 62, 13, 3, 19, 5, 1],
      [15, 20, 10, 41, 7, 92, 32, 5],
      [17, 3, 11, 1, 7, 32, 3, 13],
      [14, 4, 14, 1, 6, 8, 42, 2],
      [16, 19, 12, 1, 11, 91, 4, 18],
      [13, 17, 15, 12, 2, 17, 51, 8],
      [8, 13, 18, 1, 8, 75, 57, 9]]


t3 = [[6, 6, 6, 6, 6, 6, 6, 6],
      [81, 13, 62, 24, 3, 19, 5, 6],
      [15, 20, 10, 41, 7, 9, 19, 6],
      [17, 3, 11, 1, 7, 21, 3, 6],
      [14, 4, 14, 2, 6, 82, 48, 6],
      [16, 19, 12, 1, 11, 11, 91, 6],
      [13, 17, 15, 12, 2, 17, 22, 6],
      [8, 13, 18, 1, 8, 5, 77, 88]]

t = [[11,1],
     [51,21]]

print(zad18(t2))


'''
def valid_move(fr, to):
    last = fr % 10
    first = to // 10**int(log10(to))
    return last < first


def zad18(T,w=0,k=0):

    def rek(w,k):
        if w == k == len(T) - 1:
            return True
        moves = [(1,1),(1,0),(0,1)]
        flag = False
        for x, y in moves:
            if w+x < len(T) and k+y < len(T) and valid_move(T[w][k],T[w+x][k+y]):
                flag = flag or rek(w+x,k+y)
        return flag
    return rek(w,k)
'''
