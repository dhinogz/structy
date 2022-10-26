from node import Node


def merge_lists(head_1: Node, head_2: Node):

    dummy_head = Node(None)
    tail = dummy_head
    current1 = head_1
    current2 = head_2

    while current1 is not None and current2 is not None:

        if current1.val > current2.val:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        tail = tail.next

    if current1 is not None:
        tail.next = current1
    elif current2 is not None:
        tail.next = current2

    return dummy_head.next