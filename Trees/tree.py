class BinaryTreeNode():

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


    def insertRight(self, value):
        self.right = BinaryTreeNode(value)


    def insertLeft(self, value):
        self.left = BinaryTreeNode(value)



def depth_first_traversal(root):
    traversal_list = [root.value]

    if root.left:
        traversal_list.extend(depth_first_traversal(root.left))
    
    if root.right:
        traversal_list.extend(depth_first_traversal(root.right))

    return traversal_list
