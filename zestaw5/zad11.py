def zad11(t,do_ilu):
    n = len(t)
    result = 0
    def rek(i=0,ilo=1):
        nonlocal result
        if ilo >= do_ilu or i == n:
            if ilo == do_ilu:
                result += 1
        else:
            rek(i+1,ilo*t[i])
            rek(i+1,ilo)
    rek()
    return result


t = [2,7,3,2,4]
print(zad11(t,12))