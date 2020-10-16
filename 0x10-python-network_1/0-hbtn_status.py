#!/usr/bin/python
"""module"""


import urllib.request


req = urllib.request.Request('https://intranet.hbtn.io/status', )
with urllib.request.urlopen(req) as url:
    read = url.read()
decode = read.decode("utf-8")
print('Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'
      .format(type(read), read, decode))
