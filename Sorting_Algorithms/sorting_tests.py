import unittest
from sorting import *


class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.unsorted_list = [3, 0, 7, -2, 5, 8, 7, 6]
        self.sorted_list = [-2, 0, 3, 5, 6, 7, 7, 8]

    def test_sorting(self):
        self.assertEqual(merge_sort(self.unsorted_list), self.sorted_list)
        self.assertEqual(bubble_sort(self.unsorted_list), self.sorted_list)


if __name__ == '__main__':
    unittest.main()