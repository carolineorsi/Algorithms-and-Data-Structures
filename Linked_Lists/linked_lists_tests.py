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


if __name__ == '__main__':
    unittest.main()