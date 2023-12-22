def king(n,l):
    result = 0

    def rek(w=0,k=0,mv=0,last=""):
        nonlocal result
        if w == k == n-1:
            result = max(mv,result)
            return
        if last != "d" and w-1 >= 0 and (w-1,k) not in l:
            rek(w-1,k,mv + 1, "g")
        if last != "g" and w + 1 < n and (w+1,k) not in l:
            rek(w+1,k,mv + 1, "d")
        if k + 1 < n and (w,k+1) not in l:
            rek(w,k + 1, mv + 1, "p")
    rek()
    return result if result != 0 else None  # Wersja oszukana xd


def king2(n, l, w=0, k=0, mv=0, last=""):
    if w == k == n - 1:
        return mv
    a, b, c = 0, 0, 0
    if last != "d" and w - 1 >= 0 and (w - 1, k) not in l:
        a = king2(n, l,w - 1, k, mv + 1, "g")
    if last != "g" and w + 1 < n and (w + 1, k) not in l:
        b = king2(n, l,w + 1, k, mv + 1, "d")
    if k + 1 < n and (w, k + 1) not in l:
        c = king2(n, l,w, k + 1, mv + 1, "p")
    return max(a, b, c)  # correct version I hope


n = 8
l = [(1, 1), (2, 2), (3, 3),(4,2), (4, 4), (0, 2)]

print(king(n,l))
print(king2(n,l))