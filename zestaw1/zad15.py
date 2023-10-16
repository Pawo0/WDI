from math import sqrt
import math

def wyzn_pi():
    x = 1
    y = 0
    for i in range(1000):
        y = sqrt(0.5+0.5*y)
        x *= y
    return 2/x

print(wyzn_pi())
