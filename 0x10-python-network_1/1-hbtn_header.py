#!/usr/bin/python3
"""module"""


if __name__ == "__main__":

    import urllib.request
    import sys


    with urllib.request.urlopen(sys.argv[1]) as resp:
        res = dict(resp.info())
        print(res.get('X-Request-Id'))
