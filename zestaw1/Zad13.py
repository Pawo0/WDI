def NWD(x,y):
    if y == 0:
        return x
    else:
        return NWD(y,x%y)

def NWW(x,y):
    return abs(x*y)/NWD(x,y)

def NWW3(x,y,z):
    a = NWW(x,y)
    b = z
    return NWW(a,b)


print(NWW3(18,24,36))
print(NWW3(6,8,12))