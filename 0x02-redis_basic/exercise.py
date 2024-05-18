#!/usr/bin/env python3
""" script that writes strings to Redis """
import redis
import uuid
from typing import Union, Callable, Optional
""" imports differnt modules"""


class Cache:
    """ declares the class, Cache"""
    def __init__(self):
        """Constructor Method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store method that stores input data in Redis using a
        random key, returns the key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable = None) -> Union[str, bytes, int, float]:)
    """ get method that take a key string arg, optional Callable arg called fn"""
    value = self._redis.get(key)
    if value is not None and fn:
        value = fn(value)
    return value

    def get_str(self) -> Optional[str]:
    """
    method that will automatically parametrize Cache.get
    with the correct conversion function
    """
    return self._redis.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
    """
    method that will automatically parametrize Cache.get
    with the correct conversion function
    """
    return self._redis.get(key, fn=int)
