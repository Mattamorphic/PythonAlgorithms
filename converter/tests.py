import unittest
import BaseConverter

class TestConverterFunctions(unittest.TestCase):

    def test_base_converter_binary(self):
        self.assertEqual(BaseConverter.convertTo(15, 2), '1111')


if __name__ == '__main__':
    unittest.main()
