<<<<<<< HEAD
def zad13():

    def rec(n,res,j=1):
        if n == 0:
            print(res[:-1])
            return
        for i in range(j,n+1):
            res += str(i) + "+"
            rec(n-i,res,i)
            res = ""

    rec(4,"")

zad13()
=======
def rec(x, result="", j=1):
    if x == 0:
        print(result[:-1])
        return
    for i in range(j,x+1):
        rec(x-i,result+str(i)+"+",i)

rec(10)
>>>>>>> wdi/master