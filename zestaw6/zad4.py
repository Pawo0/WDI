from lista import Node, print_list, init_natural


def list_revers(p):
    p = Node(None,p) # guard
    a = Node(p.next.val)
    p = p.next
    while p.next is not None:
        b = Node(p.next.val, a)
        a = b
        p = p.next
    return a


# o co chodzi idk xd
def rek_list_rev(p):
    if p.next is None:
        return p, p
    rev_start, rev_end = rek_list_rev(p.next)
    p.next = None
    rev_end.next = p
    return rev_start, rev_end.next


if __name__ == "__main__":
    p = init_natural(10)
    print_list(p)

    rv = list_revers(p)
    print_list(rv)

    rv = rek_list_rev(p)[0]
    print_list(rv)
