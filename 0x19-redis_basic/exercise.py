#!/usr/bin/env python3
"""module"""


import redis
import uuid
from sys import byteorder
from typing import Union, Optional, Callable, List
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
        out = method(self, *args, **kwargs
        self._redis.rpush(output, str(out))
        return out

    return wrapper

def replay(method: Callable) -> None:
    """function"""
    name = method.__self__
    count = method.__qualname__
    key_i = method.__qualname__ + ":inputs"
    key_o = method.__qualname__ + ":outputs"
    time = name.get(count).decode("utf-8")
    zipped = list(zip(name.get_list(key_i), name.get_list(key_o)))
    print(name + " was called " + time + " times:")
    for i in zipped:
        print('{}(*{}) -> {}'.format(name, i[0].decode("utf-8"), 
                                     i[1].decode("utf-8"))


class Cache:
    """this is a class"""

    def __init__(self) -> None:
        """init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, int, float, bytes]) -> str:
        """method"""
        val = str(uuid.uuid4())
        self._redis.set(val, data)
        return val

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, 
                                                                    int, 
                                                                    float, 
                                                                    bytes]:
        """method"""
        res = self._redis.get(key)
        if fn:
            res = fn(res) 
        return res

    def get_list(self, key: str) -> List:
        """returns list"""
        return self._redis.lrange(key, 0, -1)

    def get_str(b: bytes) -> str:
        """returns string"""
        return b.decode("utf-8")

    def get_int(b: bytes) -> str:
        """returns int"""
        return int.from_bytes(b, byteorder)
