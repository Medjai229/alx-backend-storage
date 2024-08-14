#!/usr/bin/env python3
""" A python script that interacts with redis database """
import redis
import requests
from typing import Callable
from functools import wraps


r = redis.Redis()


def cache_with_count(method: Callable) -> Callable:
    """
    A decorator that caches the result of a given method and counts
    the number of times the result is retrieved.
    """

    @wraps(method)
    def invoker(url) -> str:
        """
        A wrapper function that caches the result of a given method
        and counts the number of times the result is retrieved.
        """

        r.incr(f'count:{url}')
        result = r.get(f'result:{url}')

        if result:
            return result.decode('UTF-8')

        result = method(url)
        r.set(f'count:{url}', 0)
        r.setex(f'result:{url}', 10, result)

        return result

    return invoker


@cache_with_count
def get_page(url: str) -> str:
    """
    Retrieves the content of a webpage at a given URL.
    """

    return requests.get(url).text
