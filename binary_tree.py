class BinaryTree:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.insert(value)

        elif value > self.value:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.insert(value)


def BT_to_list(node: BinaryTree, list_to_fill=None):
    data = [] if list_to_fill is None else list_to_fill

    if node is None:
        return

    if node.left is None and node.right is None:
        data.append(node.value)
        return

    BT_to_list(node.left, data)
    data.append(node.value)
    BT_to_list(node.right, data)

    return data
