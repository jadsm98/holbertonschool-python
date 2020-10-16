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
        print('[{}] {}'.format(dict(r.json()).get('id'), dict(r.json()).get('                               name')))
    except ValueError:
        if r.status_code == 204:
            print('No result')
        else:
            print('Not a valid JSON')
