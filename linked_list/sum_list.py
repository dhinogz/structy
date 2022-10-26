from node import Node


def sum_list(head: Node) -> int:
    sum = 0
    current = head
    while current is not None:
        sum += current.val
        current = current.next 
    return sum