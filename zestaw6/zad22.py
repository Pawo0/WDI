from lista import Node, init_natural, print_list


def is_cycle(p:Node) -> bool:
    w = p
    z = p
    while w.next is not None and w.next.next is not None:
        w = w.next.next
        z = z.next
        if w == z:
            return True
    return False



def test_cycle():
    a = Node(6)
    b = Node(5,a)
    c = Node(4,b)
    d = Node(3,c)
    e = Node(2,d)
    f = Node(1,e)
    a.next = d
    return f


def print_list_cycle(p,n=20):
    if is_cycle(p):
        for i in range(n):
            print(p.val, end=" -> ")
            p = p.next
        print("END")
    else:
        print("This is not a cycle")
        print("-"*10)
        print_list(p)
        print("-"*10)


if __name__ == "__main__":
    p = test_cycle()
    print_list_cycle(p)
    print(is_cycle(p))

    q = init_natural()
    print_list(q)
    print(is_cycle(q))

