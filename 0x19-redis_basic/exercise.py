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

    def store(self, data: str) -> str:
        """method"""
        id = uuid.uuid1()
        self._redis.set(id.int, data)
        return str(id)

    def get(self, key: str, fn=None):
        """method"""
        if fn == 'str':
            return str(self._redis.get(key))
        elif fn == 'int':
            return int(self._redis.get(key))
        elif fn == 'float':
            return float(self._redis.get(key))
        return self._redis.get(key)
