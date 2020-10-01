#!/usr/bin/python3
"""module save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """function save_to_json_file"""

    with open(filename, "a+") as f:
        return f.write(json.dumps(my_obj))
