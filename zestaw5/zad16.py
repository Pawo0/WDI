def czy_samo(n):
    samogloski = ["a","e","i","o","u","y"]
    return 1 if n in samogloski else 0


def wart_ascii(n):
    return ord(n)


def wyraz(s1,s2):
    sum_samo = 0
    sum_ascii = 0
    n = len(s2)
    for i in s1:
        sum_samo += czy_samo(i)
        sum_ascii += wart_ascii(i)

    def rek(ss=0, sa=0, id=0, res=""):
        if id == n:
            return ss == sum_samo and sa == sum_ascii and res
        return rek(ss + czy_samo(s2[id]), sa + wart_ascii(s2[id]), id + 1, res + s2[id]) or rek(ss, sa, id+1, res)

    return rek()


print(wyraz("ula","exddfdfde"))
