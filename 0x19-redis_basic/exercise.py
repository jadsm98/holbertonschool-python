#!/usr/bin/env python3
"""module"""


import redis
import uuid


class Cache:
    """this is a class"""

    def __init__(self):
        """init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """method"""
        id = uuid.uuid1()
        self._redis.set(id.int, data)
        return id.int
