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

    @patch('get_json', return_value=[{'name': 'google'}])
    def test_public_repos(self, mock_org):
        """
        test method
        """

        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_get:
            mock_get.return_value = 'https://github.com/google'
            test = GithubOrgClient('google')
            ret = test.public_repos()
            self.assertEqual(ret, ['google'])
            mock_org.assert_called_once()
            mock_get.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, license_key, expected_return):
        """ test GithubOrgClient.has_license"""
        test_client = GithubOrgClient("twitter")
        test_return = test_client.has_license(repo, license_key)
        self.assertEqual(expected_return, test_return)


@parameterized.expand([
    ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ class TestIntegrationGithubOrgClient """
    @classmethod
    def setUpClass(cls):
        """set up class"""
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """tear down class"""
        cls.get_patcher.stop()
