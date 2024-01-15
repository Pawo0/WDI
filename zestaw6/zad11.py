from lista import Node, print_list, int_to_linked


def add_del(p:Node, key:int):
    p = Node(None,p) if p.val is not None else p # guard // zeby zadzialal trzeba zwrocic xd
    appeared = False
    while p.next is not None:
        if p.next.val == key:
            p.next = p.next.next
            appeared = True
        else:
            p = p.next
    if not appeared:
        p.next = Node(key)


if __name__ == "__main__":
    p = int_to_linked(23476345)
    p = Node(None,p)
    print_list(p)

    add_del(p,5)
    print_list(p)

    add_del(p,3)
    print_list(p)

    add_del(p,9)
    print_list(p)

