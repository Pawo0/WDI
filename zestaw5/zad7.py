def zad7(T,x):
    n = len(T)

    def rec(masa=x,i=0):
        if masa == 0:
            return True
        if i >= n or masa < 0:
            return False
        return rec(masa-T[i],i+1) or rec(masa,i+1)

    return rec()



tab = [10,20,5,2]
print(zad7(tab,17))