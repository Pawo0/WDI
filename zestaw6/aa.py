from random import randrange
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
def init_rand(n=10,x=1,y=100):
    """Create linked list with n random numbers i range (x,y)"""
    a = Node(randrange(x,y))
    for i in range(n-1,-1,-1):
        b = Node(randrange(x,y),a)
        a = b
    return a

def print_list(p):
    """printing list lol"""
    while p is not None:
        print(p.val, end=" -> ")
        p = p.next
    print("END")

def print_sorted(p,k,i):
    print(i, end=": ")
    while p is not None:
        print(p.val, end=" -> ")
        p = p.next
    print("END")

def seperate(p):
    tp = [None for _ in range(10)]
    tk = [None for _ in range(10)]
    while p is not None:
        digit = p.val % 10
        if tp[digit] is None:
            tp[digit] = p
            tk[digit] = p
        else:
            tk[digit].next = p
            tk[digit] = p
        if p.next is  None:
            break
        p = p.next
    for i in range(10):
        if tp[i] is not None: tk[i].next = None
    return tp, tk

def merge(tp,tk):
    pocz = None
    kon = None
    for i in range(10):
        if tp[i] is not None:
            if pocz is None:
                pocz = tp[i]
                kon = tk[i]
            else:
                kon.next = tp[i]
                kon = tk[i]
    kon.next = None
    return pocz

if __name__ == "__main__":
    p = init_rand()
    print_list(p)
    tp, tk = seperate(p)
    print("*"*30)
    for i in range(10):
        print_sorted(tp[i], tk[i], i)
    print("*"*30)
    print_list(merge(tp, tk))