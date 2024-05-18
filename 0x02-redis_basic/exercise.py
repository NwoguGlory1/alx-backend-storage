#!/usr/bin/env python3
""" script that writes strings to Redis """
import redis
import uuid
from typing import Union
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
