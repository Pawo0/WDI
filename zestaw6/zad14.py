from lista import Node, print_list, tab_to_linked


def zad14(p:Node):
    p = Node(None,p) if p.val is not None else p
    res = p
    while p.next is not None and p.next.next is not None:
        if p.next.next.val % p.next.val == 0:
            p.next = p.next.next
        else:
            p = p.next
    return res.next


if __name__ == "__main__":
    t = [2,2,3,6,4,8,4]
    p = tab_to_linked(t)
    print_list(p)
    p = zad14(p)
    print_list(p)