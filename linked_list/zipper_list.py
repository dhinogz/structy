from node import Node
from traversal import print_list


def zipper_lists(head_1, head_2):

    # Reassing pointers in a zipper fashion

    tail = head_1
    current1 = head_1.next
    current2 = head_2
    count = 0
    while current1 is not None and current2 is not None:
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        tail = tail.next
        count += 1

    if current1 is not None:
        tail.next = current1
    if current2 is not None:
        tail.next = current2

    return head_1