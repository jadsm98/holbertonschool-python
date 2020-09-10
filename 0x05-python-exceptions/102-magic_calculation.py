#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1,3):
        try:
            if i > a:
                Exception = 'Too far'
                raise
            result += (a ** b / i)
        except:
            result = a + b
    return result
