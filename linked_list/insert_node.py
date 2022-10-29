from node import Node

def insert_node(head, value, index):

    if index == 0:
        new_head = Node(value)
        new_head.next = head
        return new_head

    count = 0
    current = head

    while current is not None:
        if count == index - 1:
            next = current.next
            current.next = Node(value)
            current.next.next = next
            return head

        count += 1
        current = current.next

    return head
