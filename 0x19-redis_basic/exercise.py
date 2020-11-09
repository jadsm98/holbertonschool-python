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

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wraps"""
        self._redis.incr(key)
        return method(*args, **kwds)

    return wrapper

def call_history(method: Callable) -> Callable:
    """decorator"""
    input = method.__qualname__ + ":inputs"
    output = method.__qualname__ + ":outputs"
    
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper"""
        self._redis.rpush(input, str(args))
        out = call_history(method)
        self._redis.rpush(output, out)
        return method(*args, **kwargs)

    return wrapper

def replay(method: Callable) -> None:
    """function"""
    name = method.__self__
    key_i = method.__qualname__ + ":inputs"
    key_o = method.__qualname__ + ":outputs"
    zipped = zip(name.self._redis.lrange(key_i, 0, -1),
                 name.self._redis.lrange(key_i, 0, -1))
    print(name + " was called " + 
          name.get(method.__qualname__).decode("utf-8") + " times:")
    for i in list(zipped):
        print('{}(*{}) -> {}'.format(name, i[0].decode("utf-8"), 
                                     i[1].decode("utf-8"))


class Cache:
    """this is a class"""

    def __init__(self) -> None:
        """init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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

cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)