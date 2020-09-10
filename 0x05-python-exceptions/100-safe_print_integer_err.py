#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print('{:d}'.format(value))
    except ValueError as err:
        sys.stderr.write('Exception: ', err)
        return False
    else:
        return True
