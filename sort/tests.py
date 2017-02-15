import unittest
import BubbleSort
import MergeSort
import QuickSort
import SelectionSort
import ShellSort

class TestSortFunctions(unittest.TestCase):

    def test_bubble_sort(self):
        aList = list("matthew")
        self.assertEqual(BubbleSort.sort(aList), ['a', 'e', 'h', 'm', 't', 't', 'w'])


    def test_merge_sort(self):
        aList = list('matthew')
        self.assertEqual(MergeSort.sort(aList), ['a', 'e', 'h', 'm', 't', 't', 'w'])

    def test_quick_sort(self):
        aList = list('matthew')
        self.assertEqual(QuickSort.sort(aList), ['a', 'e', 'h', 'm', 't', 't', 'w'])

    def test_selection_sort(self):
        aList = list('matthew')
        self.assertEqual(SelectionSort.sort(aList), ['a', 'e', 'h', 'm', 't', 't', 'w'])

    def test_shell_sort(self):
        aList = list('matthew')
        self.assertEqual(ShellSort.sort(aList), ['a', 'e', 'h', 'm', 't', 't', 'w'])

if __name__ == '__main__':
    unittest.main()
