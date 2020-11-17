#!/usr/bin/python3
"""
module
"""


import unittest


class TestAccessNestedMap(unittest.TestCase):
    """
    unit testing for access_nested_map function
    """

    @parametrized.expand
    def test_access_nested_map(self):
        """
        Test case
        """
        self.assertEqual(access_nested_map({"a": {"b": 2}}, "a"), {"b": 2})
        self.assertEqual(access_nested_map({"a": {"b": 2}}, ("a", "b")), 2)
