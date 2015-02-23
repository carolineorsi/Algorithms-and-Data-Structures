import unittest
from product_of_other_nums import *


class TestTrees(unittest.TestCase):

    def setUp(self):
        self.lst1 = [1, 7, 3, 4]
        self.lst2 = [1, 10, -5, -1, -100]

    def test_product_of_other_nums(self):
        self.assertEqual(product_of_other_nums(self.lst1), [84, 12, 28, 21])

    def test_highest_product_of_three(self):
        self.assertEqual(highest_product_of_three(self.lst1), 84)
        self.assertEqual(highest_product_of_three(self.lst2), 5000)

if __name__ == '__main__':
    unittest.main()