def rook(n,l):
    def rek(w=0,k=0,moves=0):
        mini = float('inf')
        if w == k == n - 1:
            return moves
        if w >= n or k >= n:
            return float('inf')
        for i in range(k+1,n):
            if (w,i) in l:
                break
            mini = min(mini,rek(w,i,moves+1))
        for i in range(w+1,n):
            if (i,k) in l:
                break
            mini = min(mini, rek(i, k, moves + 1))
        return mini
    return rek()

l = [(5,0),(3,3),(0,1),(5,4)]
print(rook(8,l))