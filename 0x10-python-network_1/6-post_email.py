#!/usr/bin/python3
"""module"""


if __name__ == '__main__':

    import requests
    import sys

    email = {'email': sys.argv[2]}
    url = sys.argv[1]
    r = requests.post(url, data=email)
    print(r.text)
