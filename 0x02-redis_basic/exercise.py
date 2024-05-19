""" Script that writes strings to Redis """
import redis
import uuid
from typing import Union, Callable, Optional

class Cache:
    """Declares the class Cache"""
    def __init__(self):
        """Constructor Method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method that stores input data in Redis using a
        random key, returns the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Union[str, bytes, int, float]]] = None) -> Union[str, bytes, int, float, None]:
        """Method that takes a key string arg, optional Callable arg called fn"""
        value = self._redis.get(key)
        if value is not None and fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Method that will automatically parametrize Cache.get
        with the correct conversion function for strings
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Method that will automatically parametrize Cache.get
        with the correct conversion function for integers
        """
        return self.get(key, fn=lambda d: int(d.decode("utf-8")))

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
