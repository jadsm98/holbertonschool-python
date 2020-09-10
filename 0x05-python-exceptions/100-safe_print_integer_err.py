#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print('{:d}'.format(value))
    except ValueError as err:
        print('Exception: ', err, file=stderr)
        return False
    else:
        return True
