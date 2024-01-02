def zad11(t,do_ilu):
    n = len(t)
    result = 0

    def rek(i=0,ilo=1,nk=""):
        nonlocal result
        if ilo >= do_ilu or i == n:
            if ilo == do_ilu:
                print(nk[:-1],"=",do_ilu)
                result += 1
        else:
            rek(i+1,ilo*t[i],nk+str(t[i])+"*")
            rek(i+1,ilo,nk)
    rek()
    return result


if __name__ == "__main__":
    t = [2,7,3,2,4]
    print(zad11(t,12))



