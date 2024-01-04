def is_prime(n):
    if n == 2 or n == 3:
        return 1
    if n == 0 or n % 2 == 0 or n % 3 == 0 or n == 1:
        return 0
    i = 5
    while i <= int(n**0.5):
        if n % i == 0:
            return 0
        i += 2
        if n % i == 0:
            return 0
        i += 4
    return 1


def rek2(t,ind=1):
    if ind == 9:
        print(t)
        return True
    i = 1
    while i < 10:
        if abs(t[ind-1]-i) >= 2 and not is_prime(t[ind-1]) == is_prime(i) == 1 and i not in t:
            t[ind] = i
            rek2(t,ind+1)
            t[ind] = 0
        i+=1
    return False


def rek(t, i,used=[], fr=1, last=0):
    if i == 9:
        print(t)
        return 1
    for j in range(fr, 10):
        if (last == 0 or abs(last - j) >= 2) and j not in used:
            if is_prime(last) == is_prime(j) == 1:
                rek(t, i,used, fr + 1, last)
            else:
                t[i] = j
                rek(t, i + 1,used+[j], 1, j)
                t[i] = 0
        else:
            rek(t, i,used, fr + 1, last)
    return 0

if __name__ == "__main__":
    t = [0 for i in range(9)]
    t[0] = 1
    # rek(t,0)

    rek2(t,)
