from math import sqrt


def czy_pierwsza(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0 or x == 1:
        return False
    i = 5
    while i <= sqrt(x):
        if x % i == 0:
            return False
        i += 2
        if x % i == 0:
            return False
        i += 4
    return True


def nwd(x,y):
    if y > 0:
        return nwd(y, x%y)
    return x


def wspolnoczynnikowa_v2(x,y):
    return czy_pierwsza(nwd(x,y))


def wspolnoczynnikowa(x,y):
    cnt = 0
    i = 2
    while x != 1 and y != 1:
        cnt_x = 0
        while x % i == 0:
            x /= i
            cnt_x += 1

        cnt_y = 0
        while y % i == 0:
            y /= i
            cnt_y += 1

        cnt += min(cnt_x, cnt_y)
        if cnt > 1:
            return False
        i += 1
    return cnt == 1

def four(t):
    n = len(t)
    cnt = 0
    for i in range(1,n-1):
        for j in range(1,n-1):
            if (wspolnoczynnikowa(t[i][j],t[i-1][j]) and wspolnoczynnikowa(t[i][j],t[i+1][j])
                    and wspolnoczynnikowa(t[i][j],t[i][j-1]) and wspolnoczynnikowa(t[i][j],t[i][j+1])):
                cnt += 1
    return cnt