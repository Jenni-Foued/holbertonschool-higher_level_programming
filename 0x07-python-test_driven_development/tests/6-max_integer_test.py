#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    unittest class for max_integer
    """
    def test_module_doc(self):
        """Test module docstring"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_doc(self):
        """Test function docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

if __name__ == "__main__":
    unittest.main()
