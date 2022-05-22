class BST:
    # Binary Search Tree
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)

        elif value > self.value:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def search(root, value):
    if root is None:
        return False

    elif value == root.value:
        return root

    elif value > root.value:
        return search(root.right, value)

    elif value < root.value:
        return search(root.left, value)

    else:
        return False


def to_list(node: BST, list_to_fill=None):
    data = [] if list_to_fill is None else list_to_fill

    if node is None:
        return

    if node.left is None and node.right is None:
        data.append(node.value)
        return

    to_list(node.left, data)
    data.append(node.value)
    to_list(node.right, data)

    return data
