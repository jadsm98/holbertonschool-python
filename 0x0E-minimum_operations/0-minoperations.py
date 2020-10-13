#!/usr/bin/python3
"""module"""


def minOperations(n):
    div = []
    for i in range(2, n + 1):
        if n % i == 0:
            div.append(i)
    print(div)
    a = 2
    res = 2
    for i in div:
        while a < i:
            numb = a
            if a > n:
                break
            if i % a == 0:
                a *= int(i/numb)
                res += int(i/numb)
            else:
                a += 1
                res += 1
    return res
