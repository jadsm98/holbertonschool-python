#!/usr/bin/python3
"""module"""


if __name__ == '_main__':

    import requests
    import sys

    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)
