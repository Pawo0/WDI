def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0 or x == 1:
        return False
    i = 5
    while i <= x**0.5:
        if x % i == 0:
            return False
        i += 2
        if x % i == 0:
            return False
        i += 4
    return True


def zad(t):
    n = len(t)
    x = [-2, -1, 1, 2, 2, 1, -1, -2]
    y = [1, 2, 2, 1, -1, -2, -2, -1]

    def rek(w=0,k=0):
        if w == n or k == n:
            return False
        for i in range(8):
            w2 = w+x[i]
            k2 = k+y[i]
            if 0 <= w2 < n and 0 <= k2 < n:
                if is_prime(t[w][k] + t[w2][k2]):
                    print(w,k,w2,k2)
                    return True
        return rek(w+1,k) or rek(w,k+1)

    return rek()


if __name__ == "__main__":
    t = [
  [4, 0, 0, 0, 0],
  [1, 0, 0, 0, 0],
  [0, 0, 4, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 6]
]
    print(zad(t))
