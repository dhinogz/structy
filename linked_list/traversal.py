from node import Node

a = Node(5)
b = Node(4)
c = Node(7)
d = Node(1)

a.next = b 
b.next = c 
c.next = d

def print_list(head: Node, recursive=False):
    if recursive:
        if head is None:
            return
        print(head.val)
        print_list(head.next)
    else:
        curr = head
        while curr is not None:
            print(curr.val)
            curr = curr.next


print_list(a)

