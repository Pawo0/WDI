def napraw(ogrod):
    n = len(ogrod)
    ruchy = [(0,-1),(-1,0),(0,1),(1,0)]

    def rek(w,k,zmien,kier=3):
        if len(zmien) == 3:
            return False
        if w == n and k == n - 1:
            print(zmien)
            return True
        if w == n or k == n:
            return False

        if ogrod[w][k] == "":
            return rek(w+ruchy[kier][0], k+ruchy[kier][1], zmien, kier)

        if ogrod[w][k] == "\\":
            n_kier = (kier + (1 if kier % 2 == 0 else -1) ) % 4
            n_kier_z = (kier + (1 if kier % 2 == 1 else -1) ) % 4
            return (rek(w+ruchy[n_kier][0], k+ ruchy[n_kier][1],zmien,n_kier)
                    or rek(w+ruchy[n_kier_z][0], k+ ruchy[n_kier_z][1],zmien+[(w,k)],n_kier_z))

        if ogrod[w][k] == "/":
            n_kier = (kier + (1 if kier % 2 == 1 else -1) ) % 4
            n_kier_z = (kier + (1 if kier % 2 == 0 else -1) ) % 4
            return (rek(w+ruchy[n_kier][0], k+ ruchy[n_kier][1],zmien,n_kier)
                    or rek(w+ruchy[n_kier_z][0], k+ ruchy[n_kier_z][1],zmien+[(w,k)],n_kier_z))

    return rek(0,0,[])



t = [['', '', '', '', ''],
     ['', '/', '', '/', ''],
     ['', '', '', '', ''],
     ['\\', '', '', '\\', ''],
     ['', '\\', '', '', '\\']
     ]

napraw(t)


"""
    [['', '', '', '', ''],
     ['', '/', '', '\\', ''],
     ['', '', '', '', ''],
     ['\\', '', '', '/', ''],
     ['', '\\', '', '', '\\']
     ]
"""