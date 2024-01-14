from random import randrange


class Node:
    """basic linked list, only val and next"""
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def print_list(p):
    """printing list lol"""
    while p is not None:
        print(p.val, end=" -> ")
        p = p.next
    print("END")


def init_natural(n=10):
    """Create linked list with natural numbers to n"""
    a = Node(n)
    for i in range(n-1,-1,-1):
        b = Node(i,a)
        a = b
    return a


def init_rand(n=10,x=1,y=100):
    """Create linked list with n random numbers i range (x,y)"""
    a = Node(randrange(x,y))
    for i in range(n-1,-1,-1):
        b = Node(randrange(x,y),a)
        a = b
    return a


def init_number(n):
    a = Node(n%10)
    n //= 10
    while n != 0:
        digit = n%10
        b = Node(digit,a)
        a = b
        n //= 10
    return a


def add_to_end_list(p,what):
    p = Node(None,p) # guard
    start = p.next
    while p.next is not None:
        p = p.next
    p.next = Node(what)
    return start


def remove_element(p,what):
    p = Node(None,p) # guard
    start = p.next
    while p.next is not None:
        if p.next.val == what:
            p.next = p.next.next
            return start
        p = p.next
    return start


if __name__ == "__main__":
    c = Node(3)
    b = Node(2, c)
    a = Node(1, b)

    print_list(a)
    a = add_to_end_list(a,5)
    print_list(a)
    a = remove_element(a,2)
    print_list(a)