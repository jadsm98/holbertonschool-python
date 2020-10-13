#!/usr/bin/python3
"""module"""


def minOperations(n):
    if not type(n) is int or n < 1:
        return 0
    div = []
    for i in range(2, n + 1):
        if n % i == 0:
            div.append(i)
    a = 2
    res = 2
    for j, i in enumerate(div):
        while a < i:
            numb = a
            if a > n:
                break
            if i % a == 0:
                a *= int(i/numb)
                res += int(i/numb)
            elif div[j + 1] % a == 0:
                a *= int(div[j + 1]/numb)
                res += int(div[j + 1]/numb)
            else:
                a += 1
                res += 1
    return res
