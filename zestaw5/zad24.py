from math import sqrt


def center_points(points):
    n = len(points)
    x, y = 0, 0
    for i in points:
        x += i[0]
        y += i[1]
    return x / n, y / n


def distance(p1,p2):
    x = abs(p1[0]-p2[0])**2
    y = abs(p1[1]-p2[1])**2
    return sqrt(x+y)


def zad24(t):
    n = len(t)
    result = float('inf')
    precis = ""

    def rek(i,zb1,zb2):
        nonlocal result, precis
        if i == n :
            if len(zb1) != 0 and len(zb2) != 0:
                x = center_points(zb1)
                y = center_points(zb2)
                result = min(result, distance(x,y))
                if result == distance(x,y):
                    precis = f"{zb1} i {zb2}"
        else:
            zb1.append(t[i])
            rek(i+1,zb1,zb2)
            zb1.pop()

            zb2.append(t[i])
            rek(i+1,zb1,zb2)
            zb2.pop()

            rek(i+1,zb1,zb2)
    rek(0,[],[])

    print(precis)
    return result


T = [(1.0, 2.0), (3.0, 4.0), (5.0, 7.0), (7.0, 8.0)]
print(zad24(T))


# def zad24(t):
#     n = len(t)
#     result = float('inf')
#     def rek(i,zb1,zb2):
#         nonlocal result
#         if i == n:
#             x = center_points(zb1)
#             y = center_points(zb2)
#             result = min(result, distance(x,y))
#         else:
#             zb1[i] = t[i]
#             rek(i+1,zb1,zb2)
#             zb1[i] = (0,0)
#             zb2[i] = t[i]
#             rek(i+1,zb1,zb2)
#             zb2[i] = (0,0)
#             rek(i+1,zb1,zb2)
#     zb1 = [(0,0)]*n
#     zb2 = [(0,0)]*n
#     rek(0,zb1,zb2)
#     return result
