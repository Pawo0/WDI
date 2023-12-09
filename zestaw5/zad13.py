def zad13():

    def rec(n,res,j=1):
        if n == 0:
            print(res[:-1])
            return
        for i in range(j,n+1):
            rec(n-i,res+str(i) + "+",i)

    rec(4,"")

zad13()
