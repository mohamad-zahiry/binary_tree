class BinaryTree:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def child(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.child(value)

        elif value > self.value:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.child(value)
