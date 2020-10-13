#!/usr/bin/python3
"""module"""


def minOperations(n):
    """minimum operations"""

    if n <= 1:
        return 0
    div = []
    for i in range(2, n + 1):
        if n % i == 0:
            div.append(i)
    a = 2
    res = 2
    for j, i in enumerate(div):
        while a < i:
            x = True
            numb = a
            if a > n:
                break
            for val in range(j, len(div)):
                if div[val] % a == 0:
                    a *= int(div[val]/numb)
                    res += int(div[val]/numb)
                    x = False
                    break
            if x is True:
                a += 1
                res += 1
    return res
