def zad3(t):
    n = len(t)

    def rek(w=0,s=0,last=(-10,-10),j=0,moves=[]):
        if w == n:
            if s == 0:
                print(moves)
                return True
            return False
        for i in range(j,n):
            if abs(last[0]-i) > 2 and abs(last[1]-i) > 2:
                return rek(w+1,s+t[w][i],(last[1],i),0,moves+[i]) or rek(w,s,last,j+1,moves)
        return False

    return rek()


t = [
  [1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 1],
  [0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0],
  [-2, 0, 1, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0]
]

print(zad3(t))