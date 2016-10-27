import unittest
import SelectionSort
import MergeSort
import QuickSort

class TestSortFunctions(unittest.TestCase):

    def test_selection_sort(self):
        aList = list("matthew")
        self.assertEqual(SelectionSort.sort(aList), ['a', 'e', 'h', 'm', 't', 't', 'w'])


    def test_merge_sort(self):
        aList = list('matthew')
        self.assertEqual(MergeSort.sort(aList), ['a', 'e', 'h', 'm', 't', 't', 'w'])

    def test_quick_sort(self):
        aList = list('matthew')
        self.assertEqual(QuickSort.sort(aList), ['a', 'e', 'h', 'm', 't', 't', 'w'])


if __name__ == '__main__':
    unittest.main()
