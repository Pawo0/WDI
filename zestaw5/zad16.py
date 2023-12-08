def samo(ch):
    samogloski = ["a", "e", "i", "o", "u", "y"]
    return ch in samogloski


def zad16(s1,s2):
    samo_s1 = 0
    ascii_s1 = 0
    for i in range(len(s1)):
        if samo(s1[i]):
            samo_s1 += 1
        ascii_s1 += ord(s1[i])

    def rec(i, s, a, res):
        if s == 0 and a == 0:
            print(res)
            return True
        if i >= len(s2):
            return False
        return rec(i+1,s-samo(s2[i]),a-ord(s2[i]),res+s2[i]) or rec(i+1,s,a,res)

    return rec(0,samo_s1,ascii_s1,"")

print(zad16("ula","echjxdgie"))