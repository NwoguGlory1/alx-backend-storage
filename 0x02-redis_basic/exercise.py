#!/usr/bin/env python3
""" Script that writes strings to Redis """
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps
""" imports necessary modules """


def call_history(method: Callable) -> Callable:
    """
    decorator that stores call history(inputs & ouputs) for wrapper fucntion
    """
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"
    # create key by appending :inputs to qualified name of the method

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(input_key, str(args))

        result = method(self, *args, **kwargs)

        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


def replay(fn: Callable):
    """Display the history of calls of a particular function"""
    r = redis.Redis()
    f_name = fn.__qualname__

    n_calls = r.get(f_name)
    n_calls = int(n_calls.decode('utf-8')) if n_calls else 0
    print(f'{f_name} was called {n_calls} times:')

    inputs = r.lrange(f_name + ":inputs", 0, -1)
    outputs = r.lrange(f_name + ":outputs", 0, -1)

    for i, o in zip(inputs, outputs):
        i = i.decode('utf-8')
        o = o.decode('utf-8')
        print(f'{f_name}(*{i}) -> {o}')


def count_calls(method: Callable) -> Callable:
    """ decorator function that count_calls to a method"""
    key = method.__qualname__
    """ generates a unique key using qualified name attribute"""

    @wraps(method)
    def wrapper_count_increment(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper_count_increment


class Cache:
    """Declares the class Cache"""
    def __init__(self):
        """Constructor Method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method that stores input data in Redis using a
        random key, returns the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable[[bytes], Union[str, bytes, int, float]]] =
            None) -> Union[str, bytes, int, float]:
        """ Method that takes key string arg, optional Callable arg, fn"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Method that will automatically parametrize Cache.get
        with the correct conversion function for strings
        """
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> Optional[int]:
        """
        Method that will automatically parametrize Cache.get
        with the correct conversion function for integers
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value


# Test block
if __name__ == "__main__":
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value
    print("All tests passed successfully.")

    cache.store("foo")
    cache.store("bar")
    cache.store(42)

    replay(cache.store)
