import unittest
import BinarySearch

class TestSearchFunctions(unittest.TestCase):

    def test_binary_search_in_list(self):
        aList = ['a', 'b', 'c', 'd', 'e']
        aItem = 'd'

        self.assertEqual(BinarySearch.search(aItem, aList), 3)

    def test_binary_search_not_in_list(self):
        aList = ['a', 'b', 'c', 'd', 'e']
        aItem = 'x'
        self.assertFalse(BinarySearch.search(aItem, aList))

    def test_binary_search_edge_case_left(self):
        aList = ['a', 'b', 'c', 'd', 'e']
        aItem = 'a'
        self.assertEqual(BinarySearch.search(aItem, aList), 0)

    def test_binary_search_edge_case_right(self):
        aList = ['a', 'b', 'c', 'd', 'e']
        aItem = 'e'
        self.assertEqual(BinarySearch.search(aItem, aList), 4)

    def test_binary_search_1_element(self):
        aList = ['a']
        aItem = 'x'
        self.assertFalse(BinarySearch.search(aItem, aList))

if __name__ == '__main__':
    unittest.main()
