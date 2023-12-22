def check(t,w,k,n):
    moves = ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1))
    for i, j in moves:
        if 0 <= w+i < n and 0 <= k+j < n and t[w+i][k+j] == 0:
            t[w+i][k+j] = -1


def place(t):
    n = len(t)
    result = (-1,-1)
    distance = float('inf')
    for i in range(n):
        for j in range(n):
            if t[i][j] == 1:
                check(t,i,j,n)
    def rek(w,k):
        pass


t = [[0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0],
     [0,0,1,0,0,0,0],
     [1,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,1,0],
     [0,0,0,0,0,0,0]
     ]

place(t)