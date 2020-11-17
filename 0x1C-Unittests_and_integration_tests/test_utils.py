#!/usr/bin/env python3
"""
module
"""


from parametrized import parametrized
from utils import access_nested_map
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """
    unit testing for access_nested_map function
    """

    @parametrized.expand([
        ({"a": 1}, ("a",), 1), 
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
         ])
    def test_access_nested_map(self, in1, in2, out):
        """
        Test case
        """
        self.assertEqual(self.access_nested_map(in1, in2), out)
