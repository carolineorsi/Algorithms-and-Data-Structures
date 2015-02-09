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


def depth_first_search(root, value):
    if root.value == value:
        return True

    if root.left:
        return depth_first_search(root.left, value)
    if root.right: 
        return depth_first_search(root.right, value)

    return False


def breadth_first_traversal(root):
    queue = [root]
    traversal_list = []

    while queue:
        next = queue.pop(0)
        traversal_list.append(next.value)

        if next.left:
            queue.append(next.left)
        if next.right:
            queue.append(next.right)

    return traversal_list
