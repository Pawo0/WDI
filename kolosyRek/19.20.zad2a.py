def A(x):
    return x+3


def B(x):
    return 2*x


def C(x):
    result = 0
    i = 1
    while x:
        digit = x % 10
        x //= 10
        if digit % 2 == 0:
            result = result + (digit + 1) * i
        else:
            result = result + digit * i
        i *= 10
    return result


def zad_v2(x,y,n):
    def rek(x,y,n,prev="",res=""):
        if x == y:
            print(res)
            return 1
        if n == 0:
            return 0
        return (
            (0 if prev == "A" else rek(A(x),y,n-1,"A",res+"A"))+
            (0 if prev == "B" else rek(B(x),y,n-1,"B",res+"B"))+
            (0 if prev == "C" else rek(C(x),y,n-1,"C",res+"C"))
        )
    return rek(x,y,n)

# wersja uposledzona
def zad(x,y,n):
    result = 0
    def rek(x,y,i,last="",res=""):
        nonlocal result
        if x == y:
            result += 1
            print(res)
            return
        if i == n:
            return

        if last == "A":
            rek(B(x),y,i+1,"B",res+"B")
            rek(C(x),y,i+1,"C",res+"C")
        elif last == "B":
            rek(A(x),y,i+1,"A",res+"A")
            rek(C(x),y,i+1,"C",res+"C")
        elif last == "C":
            rek(A(x),y,i+1,"A",res+"A")
            rek(B(x),y,i+1,"B",res+"B")
        else:
            rek(A(x),y,i+1,"A",res+"A")
            rek(B(x),y,i+1,"B",res+"B")
            rek(C(x),y,i+1,"C",res+"C")
    rek(x,y,0)
    return result

print(zad_v2(11,31,4))