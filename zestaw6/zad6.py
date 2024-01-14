from lista import Node, init_natural, print_list


def add(p: Node, val):
    start = p
    while p.next is not None:
        p = p.next
    p.next = Node(val)
    return start


def add_rek(p,val):
    if p.next is None:
        p.next = Node(val)
        return p
    p.next = add_rek(p.next,val)
    return p

def first_test():
    p = init_natural()
    print_list(p)
    add(p, 69)
    print_list(p)


def second_test():
    p = init_natural()
    print_list(p)
    add_rek(p, 69)
    print_list(p)


if __name__ == "__main__":
    first_test()
    print("-"*30)
    second_test()