#!/usr/bin/python3
"""module"""


import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    res = dict(response.info())
print(res['X-Request-Id'])
