import unittest
import SelectionSort

class TestSortFunctions(unittest.TestCase):

    def test_selection_sort(self):
        aList = list("matthew")
        self.assertEqual(SelectionSort.sort(aList), ['a', 'e', 'h', 'm', 't', 't', 'w'])


if __name__ == '__main__':
    unittest.main()
