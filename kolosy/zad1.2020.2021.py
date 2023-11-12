def multi(T: list):
    maks = 0
    for napis in T:
        n = len(napis)
        i = 1
        while i <= n/2:
            if n % i == 0:
                fragment = napis[:i]
                flag = True
                j = i
                while j < n:
                    if fragment != napis[j:j+i]:
                        flag = False
                        break
                    j += i
                if flag and n > maks:
                    maks = n
                    break
            i += 1
    return maks


tab = ["DAWZ","AAAAA","ABCABCABC"]
print(multi(tab))