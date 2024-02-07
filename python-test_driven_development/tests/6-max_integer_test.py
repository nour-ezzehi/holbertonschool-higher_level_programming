#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest


max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test the max_integer function"""

    def test_max_integer(self):
        """test if integer is max integer"""
        self.assertEqual(max_integer([0, 2]), 2)
        self.assertEqual(max_integer([6, 3, 9]), 9)
        self.assertEqual(max_integer([10, 9, 7, 2, 5, 12]), 12)

    def test_none(self):
        """tests None"""
        self.assertEqual(max_integer(), None)

    def test_same_entry(self):
        """Test to check max int if same"""
        self.assertEqual(max_integer([10, 10, 10, 10]), 10)

    def test_float_integer(self):
        """Test to see if float is max integer"""
        self.assertEqual(max_integer([10.2, -8, 10]), 10.2)

    def test_one_entry(self):
        """Test a list with only one value"""
        self.assertEqual(max_integer([10]), 10)

    def test_negative_integer(self):
        """Test negative integers"""
        self.assertEqual(max_integer([-6, -1, -10]), -1)

    if __name__ == '__main__':
        unittest.main()
