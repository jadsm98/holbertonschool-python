#!/usr/bin/env python3
"""
module
"""

from parameterized import parameterized
from unittest.mock import Mock, patch, PropertyMock
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """
    unittest class for GithubOrgClient
    """

    @parameterized.expand([
        'google', 'abc'
    ])
    @patch('client.get_json', return_value={'payload': True})
    def test_org(self, inp, out):
        """
        method to test org
        """
        test = GithubOrgClient(inp)
        ret = test.org
        self.assertEqual(ret, out.return_value)
        out.assert_called_once()

    def test_public_repos_url(self):
        """
        test method
        """
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {'repos_url': 'twitter'}
            test = {'repos_url': 'twitter'}
            client = GithubOrgClient(test.get('repos_url'))
            self.assertEqual(client._public_repos_url, mock_org.return_value.get('repos_url'))
            mock_org.assert_called_once()
