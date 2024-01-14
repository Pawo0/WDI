from lista import Node, print_list, init_rand


def separate(p):
    tp = [Node() for _ in range(10)]
    tk = [n for n in tp]
    while p.next is not None:
        nex = p.next  # zapisuje nastepny zeby nie zepsuc
        digit = p.val % 10
        tk[digit].next = p
        tk[digit] = tk[digit].next
        tk[digit].next = None

        p = nex

    return tp, tk


def merge2(tp,tk):
    res = tp[0]
    last = tk[0]
    for i in range(1,10):
        last.next = tp[i].next
        if tk[i].val is not None:  # koniec wskazuje na next tylko jak nie pusty
            last = tk[i]
    return res


def show(tp,tk):
    for i, wp in enumerate(tp):
        print(i,end=": ")
        print_list(wp)

    print("*"*30)
    for i, wk in enumerate(tk):
        print(i,end=": ")
        print_list(wk)


if __name__ == "__main__":
    p = init_rand(20)
    print_list(p)
    tp, tk = separate(p)
    show(tp,tk)

    print("-"*40)
    xd = merge2(tp,tk)
    print_list(xd)

