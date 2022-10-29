from node import Node


def remove_node(head: Node, target: str) -> Node:

    if head.val == target:
        return head.next

    current = head
    prev = None

    while current is not None:
        if current.val == target:
            prev.next = current.next
            break
        prev = current
        current = current.next
    return head

def remove_node(head, target):

    if head.val == target:
      return head.next
  
    current = head
    prev = None
    
    while current is not None:
        
        if current.val == target:
            prev.next = current.next
            break
        prev = current
        current = current.next
    return head
        