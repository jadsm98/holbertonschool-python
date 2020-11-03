#!/usr/bin/env python3
""" module"""


def list_all(mongo_collection):
    """ function"""

    find = mongo_collection.find({})
    if mongo_collection == {}:
        return []
    return [doc for doc in find]
