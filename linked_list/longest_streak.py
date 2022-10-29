from node import Node


# def longest_streak(head):
#     """Space is O(n), which is not ideal. Let's look for an O(1) solution"""
#     count = {}
#     current = head
#     while current is not None:
#         if current.val not in count:
#             count[current.val] = 1
#         else:
#             count[current.val] += 1
#         current = current.next
#     return max(count)


def longest_streak(head: Node) -> int:
    """
    Space complexity O(1)
    Time complexity O(n)
    """

    longest_streak = 0
    current_streak = 0

    prev_val = None
    current = head

    while current is not None:

        if current.val == prev_val:
            current_streak += 1
        else:
            current_streak = 1
        
        longest_streak = max(current_streak, longest_streak)

        prev_val = current.val
        current = current.next

    return longest_streak


a = Node(1)
b = Node(1)
c = Node(1)
d = Node(2)
f = Node(10)

a.next = b
b.next = c
c.next = d
d.next = f

print(longest_streak(a))
