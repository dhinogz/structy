from node import Node


def get_node_value(head, index):
    # Iterative
    # O(n) Time
    # O(1) Space
    i = 0
    current = head
    while i is not None:
        if i == index:
            return current.val

        current = current.next
        i += 1

    return None


def get_node_value(head, index):
  
  if head is None:
    return None
  if index == 0:
    return head.val
  
  return get_node_value(head.next, index-1)
  