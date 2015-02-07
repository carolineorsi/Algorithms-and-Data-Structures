import unittest
from tree import *


class TestTrees(unittest.TestCase):

    def setUp(self):
        self.tree = BinaryTreeNode(1)
        self.tree.insertLeft(2)
        self.tree.insertRight(3)

    def test_right(self):
        self.assertEqual(self.tree.right.value, 3)

    def test_left(self):
        self.assertEqual(self.tree.left.value, 2)


if __name__ == '__main__':
    unittest.main()