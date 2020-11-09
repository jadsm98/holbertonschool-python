#!/usr/bin/env python3
"""module"""


import redis
import uuid
from sys import byteorder
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """decorator"""
    key = method.__qualname__
    @wraps(count_calls)
    def wrapper(*args, **kwds):
        """wraps"""
        self._redis.incr(key)
        return method(*args, **kwds)
    return wrapper

class Cache:
    """this is a class"""

    def __init__(self) -> None:
        """init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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

    def get_str(b: bytes) -> str:
        """returns string"""
        return b.decode("utf-8")

    def get_int(b: bytes) -> int:
        """returns int"""
        return int.from_bytes(b, byteorder='big')
