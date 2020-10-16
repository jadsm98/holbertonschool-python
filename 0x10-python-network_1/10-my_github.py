#!/usr/bin/python3
"""module"""


if __name__ == '__main__':

    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]

    r = requests.get('https://api.github.com/users/octocat')
    print(dict(r.json()).get('id'))
