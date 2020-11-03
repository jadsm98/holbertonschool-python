#!/usr/bin/env python3
"""module"""


def insert_school(mongo_collection, **kwargs):
    """function"""

    x = mongo_collection.insert_one(**kwargs)
    return mongo_collection["_id"]
