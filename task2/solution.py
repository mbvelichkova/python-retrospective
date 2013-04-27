from itertools import starmap
from collections import OrderedDict


def groupby(func, seq):
    result = {}
    for iter in seq:
        result.setdefault(func(iter), []).append(iter)
    return result


def zip_with(func, *iterables):
    return starmap(func, zip(*iterables))


class Cache:
    def __init__(self, func, cache_size):
        self.cache = OrderedDict()
        self.func = func
        self.cache_size = cache_size

    def func_cached(self, *args):
        if args in self.cache:
            return self.cache[args]
        else:
            if len(self.cache) == self.cache_size:
                self.cache.popitem(False)
            result = self.func(*args)
            self.cache[args] = result
            return result


def cache(func, cache_size):
    cached = Cache(func, cache_size)
    return cached.func_cached