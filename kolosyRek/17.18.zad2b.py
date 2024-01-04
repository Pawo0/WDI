def zad(t):

    def rek(i=0, el1=0, el2=0, s1=0, s2=0):
        if i == len(t):
            return False
        if s1 == s2 != 0:
            if s1 == s2:
                return True
        return rek(i+1,el1+1,el2,s1+t[i],s2) or rek(i+1,el1,el2+1,s1,s2+t[i]) or rek(i+1,el1,el2,s1,s2)

    return rek()

if __name__ == "__main__":
    t = [1, 2, 3, 4, 5, 6, 7]
    print(zad(t))