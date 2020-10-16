#!/usr/bin/python3
"""module"""


if __name__ == '__main__':

    import requests
    import sys

    if len(sys.argv) == 1:
        res = {'q': ""}
    else:
        res = {'q': sys.argv[1]}
    r = requests.post('http://0.0.0.0:5000/search_user', data=res)
    try:
        r.json()
        print('[{}] {}'.format(dict(r.text).get('id'), dict(r.text).get('\
name')))
    except ValueError as e:
        if r.status_code == 204:
            print('No result')
        else:
            print('Not a valid JSON')
