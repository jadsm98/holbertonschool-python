#!/usr/bin/env python3
"""module"""


def update_topics(mongo_collection, name, topics):
    """function"""

    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics})
