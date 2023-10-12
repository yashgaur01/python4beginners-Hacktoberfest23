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
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursively(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursively(node.right, value)
        else:
            # Value already exists in the tree
            pass

    def search(self, value):
        return self._search_recursively(self.root, value)

    def _search_recursively(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursively(node.left, value)
        return self._search_recursively(node.right, value)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursively(self.root, result)
        return result

    def _inorder_traversal_recursively(self, node, result):
        if node:
            self._inorder_traversal_recursively(node.left, result)
            result.append(node.value)
            self._inorder_traversal_recursively(node.right, result)

# Example usage:
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print("Inorder Traversal:", tree.inorder_traversal())  # Output: [2, 3, 4, 5, 6, 7, 8]
print("Search for 4:", tree.search(4))  # Output: <__main__.Node object at 0x...>
