class BinaryTreeNode():

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insertRight(self, value):
        self.right = BinaryTreeNode(value)

    def insertLeft(self, value):
        self.left = BinaryTreeNode(value)