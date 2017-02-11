import unittest
import BinarySearch
import QuickSelect
import BasicStringSearch
import FindPairs

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
        aList = [9, 32, 20, 16, 23, 26, 8, 20, 18, 3]
        kthSmallest = 8
        self.assertEqual(QuickSelect.search(kthSmallest, aList), 23)

    def test_basic_string_search(self):
        aString = 'abcdefghijklmnopqrstuvwxyz'
        aTargetSeq = 'ghi'
        self.assertEqual(BasicStringSearch.search(aTargetSeq, aString), 6)

    def test_basic_string_search_not_found(self):
        aString = 'abcdefghijklmnopqrstuvwxyz'
        aTargetSeq = 'test'
        self.assertEqual(BasicStringSearch.search(aTargetSeq, aString), -1)

    def test_find_pairs_of_ints(self):
        k = 50
        aList = [9, 1, 11, 36, 14, 50, 9, 0, 8, 24, 22, 28, 39]
        self.assertEqual([(0, 50), (36, 14), (39, 11), (22, 28)], FindPairs.find(k, aList))

    def test_find_pairs_of_ints_single_item_list(self):
        k = 9
        aList = [9]
        self.assertEqual(None, FindPairs.find(k, aList))

    def test_find_pairs_of_ints_duplicate_item_list(self):
        k = 50
        aList = [10, 10, 20, 20, 30, 30]
        self.assertEqual([(20, 30)], FindPairs.find(k, aList))

if __name__ == '__main__':
    unittest.main()
