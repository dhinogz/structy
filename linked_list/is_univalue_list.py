from node import Node

def is_univalue_list(head):
    
    current = head

    while current is not None:
        if current.val != head.val:
            return False
        current = current.next
    return True