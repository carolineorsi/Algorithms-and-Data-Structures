import unittest
from linked_list import *


class TestLinkedLists(unittest.TestCase):

    def setUp(self):
        # placeholder
        pass

    def test_add_node(self):
        ll = LinkedList()
        ll.add_node(5)
        self.assertEqual(ll.head.value, 5)
        self.assertEqual(ll.tail.value, 5)
        ll.add_node(3)
        self.assertEqual(ll.head.value, 5)
        self.assertEqual(ll.tail.value, 3)


if __name__ == '__main__':
    unittest.main()