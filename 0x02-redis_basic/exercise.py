#!/usr/bin/env python3
""" A python script that interacts with redis database """
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    A decorator that counts the number of times a given method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        A wrapper function that increments the call count
        of a given method in Redis.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    A decorator that stores the history of
    inputs and outputs for a particular function.
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        A wrapper function that stores the input arguments
        and output data of a given method in Redis.
        """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data

    return wrapper


def replay(method: Callable) -> None:
    """
    Replays the history of a function.
    """
    name = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(name).decode('UTF-8')

    print(f'{name} was called {calls} times:')

    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)

    for input, output in zip(inputs, outputs):
        print(f'{name}(*{input.decode("UTF-8")}) -> {output.decode("UTF-8")}')


class Cache:
    """ Class Cache """

    def __init__(self):
        """
        Initializes a new instance of the Cache class.
        This method sets up a new Redis connection and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in the cache and returns the generated key.
        """
        id_key = str(uuid4())
        self._redis.set(id_key, data)
        return id_key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """
        Retrieves the value associated with the given key from the cache.
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Retrieves a string value from the Redis cache.
        """
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """
        Retrieves an integer value from the Redis cache.
        """
        value = self._redis.get(key)
        return int(value.decode('utf-8'))
