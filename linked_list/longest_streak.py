from node import Node


def longest_streak(head):

    count = {}
    current = head
    while current is not None:
        if current.val not in count:
            count[current.val] = 1
        else:
            count[current.val] += 1
        current = current.next
    return max(count)