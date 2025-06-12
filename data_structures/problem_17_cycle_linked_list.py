"""Problem 17: Detect cycle in linked list"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
