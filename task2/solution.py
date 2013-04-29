from itertools import starmap
from collections import OrderedDict


def groupby(func, seq):
    result = {}
    for iter in seq:
        result.setdefault(func(iter), []).append(iter)
    return result


def zip_with(func, *iterables):
    return starmap(func, zip(*iterables))


def cache(func, cache_size):
    if cache_size <= 0:
            return func

    cache_store = OrderedDict()

    def func_cached(*args):
        if not args in cache_store:
            if len(cache_store) == cache_size:
                cache_store.popitem(False)
            cache_store[args] = func(*args)
        return cache_store[args]

    return func_cached


def iterate(func):
    def compose(func1, func2):
        return lambda x: func1(func2(x))

    result_function = lambda x: x

    while True:
        yield result_function
        result_function = compose(result_function, func)
