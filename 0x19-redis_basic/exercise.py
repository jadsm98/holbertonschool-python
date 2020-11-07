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
        ran = str(uuid.uuid1())
        self._redis.set(ran, data)
        return self._redis.get(ran).decode("utf-8")
