#!/usr/bin/env python3
"""module"""


import redis
import uuid
from typing import Union, Optional

class Cache:
    """this is a class"""

    def __init__(self) -> None:
        """init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        """method"""
        id = uuid.uuid4()
        key = str(self._redis.set(id.int, data))
        return key

    def get(self, key: str, fn: Optional[callable] = None) -> Union[str, int, float, bytes]:
        """method"""
        return fn(self._redis.get(key))
