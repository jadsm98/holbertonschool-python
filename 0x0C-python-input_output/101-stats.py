#!/usr/bin/python3
"""module"""


import sys


x = 0
arg = 0
dic = {200: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
for line in sys.stdin:
    x += 1
    try:
        arg += int(line.split(' ')[-1])
        line.split(' ')[-2]
        for k, v in dic.items():
            if int(line.split(' ')[-2]) == k:
                dic[k] += 1
        if x % 10 == 0:
            print('File size: {}'.format(arg))
            for k in sorted(dic.items()):
                print('{}: {}'.format(k[0], k[1]))
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
