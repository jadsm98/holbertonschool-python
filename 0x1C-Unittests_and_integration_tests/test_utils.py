#!/usr/bin/env python3
"""
module
"""


from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import Mock
import requests
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
        with self.assertRaises(exception):
            access_nested_map(in1, in2)


class TestGetJson(unittest.TestCase):
    """
    test cases for get_json
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        test method
        """
        mock = Mock()
        mock.json.return_value = test_payload
        with unittest.mock.patch('requests.get', return_value=mock):
            self.assertEqual(get_json(test_url), test_payload)
            mock.assert_called_once_with(test_url)
