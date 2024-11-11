import unittest
from convert import str_to_float

class TestConvert(unittest.TestCase):
    def test_valid_float(self):
        self.assertEqual(str_to_float("3.14"), 3.14)

    def test_invalid_float(self):
        self.assertIsNone(str_to_float("xyz"))

    def test_empty_string(self):
        self.assertIsNone(str_to_float(""))

    def test_integer_string(self):
        self.assertEqual(str_to_float("42"), 42.0)

    def test_zero_string(self):
        self.assertEqual(str_to_float("0"), 0.0)

if __name__ == '__main__':
    unittest.main()

