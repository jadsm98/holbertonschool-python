#!/usr/bin/env python3
"""
module
"""


from parameterized import parameterized
from utils import access_nested_map, get_json
import unittest
import requests


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
        ("http://holberton.io" {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        test method
        """
        with unittest.mock.patch.requests.get(Mock, 'json', return_value=test_payload) as mock_requests_get:
            mock = Mock()
            mock.json(test_url)
        self.assertEqual(get_json(mock.json(test_url)), test_payload)
        mock.assert_called_once_with(test_url)
