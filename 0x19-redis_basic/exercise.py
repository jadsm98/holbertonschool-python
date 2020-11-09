#!/usr/bin/env python3
"""module"""


import redis
import uuid
from typing import Union


class Cache:
    """this is a class"""

    def __init__(self):
        """init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, float, int, bytes]) -> str:
        """method"""
        id = uuid.uuid1()
        self._redis.set(id.int, data)
        return str(id)
