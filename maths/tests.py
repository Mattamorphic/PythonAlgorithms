import unittest
import RussianMultiplication
import SumMultiplesOfTotal

class TestMultiplicationFunctions(unittest.TestCase):

    def test_russian_multiplication(self):
        self.assertEqual(945, RussianMultiplication.multiply(27, 35))

    def test_sum_multiples_of_total(self):
        self.assertEqual(15, SumMultiplesOfTotal.sum(10, [5]))

    def test_sum_multiples_of_total_two_multipliers(self):
        self.assertEqual(33, SumMultiplesOfTotal.sum(10, [3, 5]))

    def test_sum_multiples_of_total_three_multipliers(self):
        self.assertEqual(98, SumMultiplesOfTotal.sum(20, [3, 6, 5]))

if __name__ == '__main__':
    unittest.main()
