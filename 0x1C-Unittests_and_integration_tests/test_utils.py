#!/usr/bin/env python3
"""
module
"""


from utils import access_nested_map
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
