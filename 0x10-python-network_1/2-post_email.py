#!/usr/bin/python3
"""module"""


if __name__ == '__main__':

    import urllib.request
    import urllib.parse
    import sys

    data = {'email': sys.argv[2]}
    email = urllib.parse.urlencode(data)
    email = email.encode('ascii')
    url = sys.argv[1]
    res = urllib.request.Request(url, email)
    with urllib.request.urlopen(res) as req:
        print(req.decode('utf-8'))
