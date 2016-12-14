import unittest
import RussianMultiplication

class TestMultiplicationFunctions(unittest.TestCase):

    def test_xor_encrypt_works(self):
        self.assertEqual(945, RussianMultiplication.multiply(27, 35))

if __name__ == '__main__':
    unittest.main()
