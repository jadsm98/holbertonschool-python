#!/usr/bin/python3
""" module"""


def list_all(mongo_collection):
    """ function"""

    if mongo_collection == {}:
        return []
    return [doc for doc in mongo_collection]
