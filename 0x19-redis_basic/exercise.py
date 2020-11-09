#!/usr/bin/env python3
"""module"""


import redis
import uuid
from typing import Union, Optional, Callable

class Cache:
    """this is a class"""

    def __init__(self) -> None:
        """init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        """method"""
        val = str(uuid.uuid4())
        self._redis.set(val, data)
        return val


    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, int, float, bytes]:
        """method"""
        res = self._redis.get(key)
        if fn:
            res = fn(res) 
        return res
