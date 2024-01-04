def rot(T,direction,w_or_k,which):
    """direction 1 - do przodu, direction -1 - do tyłu"""
    if w_or_k == "w":
        pass
    elif w_or_k == "k":
        pass


def check_magic(T) -> bool:
    pass


def magic_after_rot(T,w_k1,w_k2,i,j):
    rot(T, 1, w_k1, i)
    rot(T, 1, w_k2, j)
    flag = check_magic(T)
    rot(T, -1, w_k2, i)
    rot(T, -1, w_k1, j)
    return flag


def magic(T):
    n = len(T)
    flag = False
    for i in range(n):
        for j in range(n):
            flag = flag or magic_after_rot(T,"w","w",i,j)
            flag = flag or magic_after_rot(T,"w","k",i,j)
            flag = flag or magic_after_rot(T,"k","w",i,j)
            flag = flag or magic_after_rot(T,"k","k",i,j)
            if flag:
                return flag
    return flag



