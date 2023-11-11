def ciag(x):
    i, y = 1, 1
    tab = list()
    while y <= x:
        y = (i*i+i+1)
        tab.insert(i-1,y)
        i += 1
    tab.pop()
    return tab

def zad7(x):
    tab_l = ciag(x)
    for liczba in tab_l:
        while liczba <= x:
            if liczba == x:
                return True
            liczba += liczba
    return False

if __name__ == "__main__":
    print(zad7(222))