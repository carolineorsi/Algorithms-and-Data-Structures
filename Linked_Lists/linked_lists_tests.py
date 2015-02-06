import unittest
from linked_list import *


class TestLinkedLists(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()
        self.ll.add_node(1)
        self.ll.add_node(2)
        self.ll.add_node(3)
        self.ll.add_node(4)
        self.ll_as_list = [1, 2, 3, 4]

    def test_add_node(self):
        ll = LinkedList()
        ll.add_node(5)
        self.assertEqual(ll.head.value, 5)
        self.assertEqual(ll.tail.value, 5)
        ll.add_node(3)
        self.assertEqual(ll.head.value, 5)
        self.assertEqual(ll.tail.value, 3)

    def test_return_list(self):
        self.assertEqual(self.ll.return_list(), self.ll_as_list)

    def test_len(self):
        self.assertEqual(len(self.ll), 4)

    def test_contains(self):
        self.assertTrue(3 in self.ll)
        self.assertFalse(6 in self.ll)

    def test_max(self):
        self.assertEqual(self.ll.max(), 4)

    def test_min(self):
        self.assertEqual(self.ll.min(), 1)

    def test_return_node_by_index(self):
        self.assertEqual(self.ll.return_node_by_index(1).value, 2)
        self.assertEqual(self.ll.return_node_by_index(2).value, 3)

    def test_remove_node(self):
        node = self.ll.return_node_by_index(2)
        remove_node(node)
        self.assertEqual(self.ll.return_list(), [1, 2, 4])


if __name__ == '__main__':
    unittest.main()