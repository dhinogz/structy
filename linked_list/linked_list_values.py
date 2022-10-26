from node import Node


a = Node(5)
b = Node(4)
c = Node(7)
d = Node(1)

a.next = b 
b.next = c 
c.next = d

def linked_list_values(head):
    values = []
    curr = head
    while curr is not None:
        values.append(curr.val)
        curr = curr.next
    return values