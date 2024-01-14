from lista import Node, init_natural, print_list


def delete(p: Node):
    start = p
    if p.next is None:
        return None
    while p.next.next is not None:
        p = p.next
    p.next = None
    return start


def rek_delete(p: Node):
    if p.next is None:
        return None
    if p.next.next is None:
        p.next = None
        return p
    return rek_delete(p.next)


if __name__ == "__main__":
    p = init_natural()
    print_list(p)
    delete(p)
    print_list(p)

    rek_delete(p)
    print_list(p)
