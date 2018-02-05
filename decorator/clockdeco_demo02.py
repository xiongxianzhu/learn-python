# coding: utf-8

import time
from wraps import functools


def clock(func):

    @wraps
    def clocked(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked



@clock
def go():
    for i in range(50):
        print(i)


if __name__ == "__main__":
    go()
