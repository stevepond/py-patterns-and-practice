"""Problem 07: Binary tree basic insert"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        cur = self.root
        while True:
            if value < cur.value:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(value)
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(value)
                    break

    def inorder(self):
        def _in(node):
            return _in(node.left) + [node.value] + _in(node.right) if node else []
        return _in(self.root)
