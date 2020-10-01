#!/usr/bin/python3
"""module load_from_json_file"""


import json


def load_from_json_file(filename):
    """function load_from_json_file"""

    with open(filename, "w+") as f:
        return json.loads(f.read())
