def zad7(T,x):
    n = len(T)

    def rec(masa=x,i=0, l_chosen=[], p_chosen=[]):
        if masa == 0:
            print(f"L: {l_chosen} P: {p_chosen}")
            return True
        if i >= n:
            return False
        return rec(masa-T[i],i+1,l_chosen+[T[i]],p_chosen) or rec(masa+T[i],i+1,l_chosen,p_chosen+[T[i]]) or rec(masa,i+1,l_chosen,p_chosen)
    return rec()



tab = [10,20,5,2]
print(zad7(tab,3))