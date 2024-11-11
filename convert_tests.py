import unittest
from convert import str_to_float

class TestConvert(unittest.TestCase):
    # Test that a valid float string is correctly converted to a float
    # Define a test case class that inherits from unittest.TestCase to organize and run the tests
    def test_valid_float(self):
        self.assertEqual(str_to_float("3.14"), 3.14)
    # Test that an invalid float string returns None
    def test_invalid_float(self):
        self.assertIsNone(str_to_float("xyz"))

    def test_empty_string(self):
        self.assertIsNone(str_to_float(""))

    # Test that a valid integer string is correctly converted to a float
    def test_integer_string(self):
        self.assertEqual(str_to_float("42"), 42.0)

    # Test that the string "0" is correctly converted to the float 0.0
    def test_zero_string(self):
        self.assertEqual(str_to_float("0"), 0.0)

if __name__ == '__main__':
    unittest.main()

