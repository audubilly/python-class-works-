import unittest
from .Binary_to_Decimal import Binary_to_Decimal


class TestBinaryToDecimal(unittest.TestCase):

    def test_binary_to_decimal_0(self):
        dec = Binary_to_Decimal(0)
        self.assertEqual(dec, 0)

    def test_binary_to_decimal_1(self):
        dec = Binary_to_Decimal(1)
        self.assertEqual(dec, 1)

    def test_binary_to_decimal_10(self):
        dec = Binary_to_Decimal(10)
        self.assertEqual(dec, 2)

    def test_binary_to_decimal_with_String(self):
        with self.assertRaises(TypeError):
            dec = Binary_to_Decimal("Hello")


if __name__ == '__main__':
    unittest.main()
