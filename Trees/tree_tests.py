import unittest
from tree import *


class TestTrees(unittest.TestCase):

    def setUp(self):
        self.tree = BinaryTreeNode(1)
        self.tree.insertLeft(2)
        self.tree.insertRight(3)

    def test_tree(self):
        self.assertEqual(self.tree.value, 1)
        self.assertEqual(self.tree.right.value, 3)
        self.assertEqual(self.tree.left.value, 2)

    def test_depth_first_traversal(self):
        self.assertEqual(depth_first_traversal(self.tree), [1, 2, 3])



if __name__ == '__main__':
    unittest.main()