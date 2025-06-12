"""Problem 06: Singly linked list"""

class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(value)

    def to_list(self):
        result = []
        cur = self.head
        while cur:
            result.append(cur.value)
            cur = cur.next
        return result
