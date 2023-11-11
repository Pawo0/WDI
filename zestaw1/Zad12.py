def NWD(x,y):
    if y == 0:
        return x
    else:
        return NWD(y,x%y)

def NWD3(x,y,z):
    a = NWD(x,y)
    b = z
    return NWD(a,b)


print(NWD3(12,6,3))