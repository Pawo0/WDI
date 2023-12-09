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


t = [1,7,3,5,11,2]
print(zad6(t))