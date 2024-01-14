from lista import Node, print_list, init_rand, add_to_end_list


def separation(p):
    tp = [None for _ in range(10)]
    tk = [None for _ in range(10)]
    while p.next is not None:
        digit = p.next.val % 10
        if tp[digit] is None:
            tp[digit] = Node(p.next.val)
            tk[digit] = Node(p.next.val)
        else:
            add_to_end_list(tp[digit], p.next.val)  # import z 'lista'
            # tp[digit] = Node(p.next.val,tp[digit]) # / alternative, but reversed
            tk[digit] = Node(p.next.val)
        p = p.next
    return tp, tk


def scale(tp,tk):
    res = Node()
    for i in range(9,-1,-1):
        res.next = tp[i]


def show(tp,tk):
    for i, wp in enumerate(tp):
        print(i,end=": ")
        print_list(wp)

    print("*"*30)
    for i, wk in enumerate(tk):
        print(i,end=": ")
        print_list(wk)


if __name__ == "__main__":
    p = init_rand()
    p = Node(None, p) # guard
    print_list(p)
    tp, tk = separation(p)
    show(tp,tk)

