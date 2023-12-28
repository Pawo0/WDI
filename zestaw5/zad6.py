from math import inf


def zad6(t):
    n = len(t)
    result = 0
    ile_min = inf
    def rek(i=0,s_id=0,s_el=0,ile=0):
        nonlocal result, ile_min
        if i == n:
            if s_el == s_id and s_el != 0 and ile <= ile_min:
                result = s_el
                ile_min = ile
            return
        if i < n:
            return rek(i+1,s_id + i, s_el + t[i],ile+1) or rek(i+1,s_id,s_el,ile)
    rek()
    return result


def zad6_v2(T):
    ile_min = float('inf')

    def rek(i=0,sum_e=0, sum_i=0,ile=0,res=[]):
        nonlocal ile_min
        if sum_e != 0 and sum_e == sum_i and ile < ile_min:
            ile_min = ile
            print(res)
            return sum_e
        if i == len(T):
            return float('inf')
        return min(rek(i+1,sum_e,sum_i,ile,res),rek(i+1,sum_e+T[i],sum_i+i,ile+1,res+[i]))
    return rek()



t = [1,7,3,5,11,2]
print(zad6(t))
print(zad6_v2(t))