#!/usr/bin/env python3
"""Module"""


def schools_by_topic(mongo_collection, topic):
    """function"""

    x = mongo_collection.find({topic: {$in: topics}})
    return x.get("name")
