from math import log10


def valid_move(T,w,k,x,y,wk,kk):
    fr = T[w][k]
    to = T[w+x][k+y]
    last = fr % 10
    first = to // 10**int(log10(to))
    return last < first and check_if_closer(w,k,wk,kk,(x,y))


def check_if_closer(w,k,wk,kk,move):
    return (w+move[0]-wk)**2 + (k+move[1]-kk)**2 < (w-wk)**2 + (k-kk)**2

def zad19(T,w=0,k=0):

    def rek(w,k,wk,kk):
        if w == wk and k == kk:
            return True
        moves = [(1, 1), (1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1)]
        flag = False
        for x, y in moves:
            if w+x < len(T) and k+y < len(T) and valid_move(T,w,k,x,y,wk,kk):
                flag = flag or rek(w+x,k+y,wk,kk)
        return flag

    corners = [(0,0),(len(T)-1,0),(0,len(T)-1),(len(T)-1,len(T)-1)]
    flag = False
    for wk, kk in corners:
        if not flag:
            flag = rek(w,k,wk,kk)
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

print(zad19(t2,4,4))