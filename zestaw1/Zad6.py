a = 1
s = 2020
eps = 1e-10


while True:
    b = (s/a + a)/2.0
    if abs(b-a) < eps:
        break
    a = b

print(a)
