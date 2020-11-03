#!/usr/bin/env python3
"""module"""


def insert_school(mongo_collection, **kwargs):
    """function"""

    x = mongo_collection.insert_one(kwargs)
    return x.inserted_id
