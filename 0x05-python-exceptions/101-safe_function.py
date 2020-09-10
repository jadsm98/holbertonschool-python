#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        ans = fct(*args)
        return ans
    except Exception as err:
        print('Exception:', err, file=stderr)
        return None
