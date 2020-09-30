#!/usr/bin/python3
"""inherits from a list"""


class MyList(list):
    """class to inherit from list"""

    def print_sorted(self):
        print(sorted(self))
