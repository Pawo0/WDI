from lista import Node, init_natural, print_list


def delete_by_2(p: Node):
    p = Node(None,p)
    start = p.next
    while True:
        p.next = p.next.next
        p = p.next
        if p is None:
            break
    return start


if __name__ == "__main__":
    p = init_natural()
    print_list(p)
    delete_by_2(p)
    print_list(p)