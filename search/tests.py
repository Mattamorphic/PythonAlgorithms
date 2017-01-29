import unittest
import BinarySearch
import QuickSelect
import BasicStringSearch

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

    def test_quick_select(self):
        aList = [5, 2, 21, 8, 20, 36, 1, 11, 13, 4, 17]
        kthSmallest = 3
        self.assertEqual(QuickSelect.search(kthSmallest, aList), 4)

    def test_basic_string_search(self):
        aString = 'abcdefghijklmnopqrstuvwxyz'
        aTargetSeq = 'ghi'
        self.assertEqual(BasicStringSearch.search(aTargetSeq, aString), 6)

    def test_basic_string_search_not_found(self):
        aString = 'abcdefghijklmnopqrstuvwxyz'
        aTargetSeq = 'test'
        self.assertEqual(BasicStringSearch.search(aTargetSeq, aString), -1)

if __name__ == '__main__':
    unittest.main()
