#!/usr/bin/python3
def no_c(my_string):
    b = list(my_string)
    for i in b:
        if i == 'c':
            b.remove('c')
        elif i == 'C':
            b.remove('C')
    return ''.join(b)
