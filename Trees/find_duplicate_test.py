import unittest
from find_duplicate import *


class TestTrees(unittest.TestCase):

    def setUp(self):
        self.lst1 = [2,3,7,9,8,4,5,6,4,1]
        self.lst2 = [2,3,7,9,8,4,2,6,4,1]

    def test_find_duplicate(self):
        self.assertEqual(find_duplicate(self.lst1), 4)
        self.assertIn(find_duplicate(self.lst2), [2,4])

if __name__ == '__main__':
    unittest.main()