from node import Node


def create(values: list):

    head = Node(values.pop(0))
    current = head

    for value in values:
        current.next = Node(value)
        current = current.next
    return head

def create(values):

    dummy_node = Node(None)
    tail = dummy_node

    for value in values:
        tail.next = Node(value)
        tail = tail.next
    return dummy_node.next