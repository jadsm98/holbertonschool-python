#!/usr/bin/env python3
"""
module
"""


from parameterized import parameterized
from utils import access_nested_map
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """
    unit testing for access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1), 
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, in1, in2, out):
        """
        Test case
        """
        self.assertEqual(access_nested_map(in1, in2), out)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, in1, in2, exception):
        """
        test case for exception
        """
        self.assertRaises(access_nested_map(in1, in2), exception)
