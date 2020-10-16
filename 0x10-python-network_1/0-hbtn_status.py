#!/usr/bin/python3
"""module"""


import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as url:
    read = url.read()
decode = read.decode("utf-8")
print('Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'
      .format(type(read), read, decode))
