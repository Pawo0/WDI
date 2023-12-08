from math import log10, floor

def rec(x,y,z=0):
    if x == 0 and y == 0:
        print(z)
    if x != 0:
        zd = z + (x%10)*(10**(floor(log10(z+0.1))+1))
        rec(x//10,y,zd)
    if y != 0:
        zd = z + (y%10)*(10**(floor(log10(z+0.1))+1))
        rec(x,y//10,zd)


rec(12,34)