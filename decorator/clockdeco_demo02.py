# coding: utf-8

"""
    一个简单的装饰器， 输出函数的运行时间。
"""


import time
from functools import wraps, lru_cache


def clock(func):

    @wraps(func)
    def clocked(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


@lru_cache()
@clock
def fibonacci(n):
    """
        生成第n个斐波纳契数

        耗时版： 不使用python3中的functools.lru_cache， 递归方式非常耗时；
        改进版： 使用python3中的functools.lru_cache实现备忘功能， 即缓存；
        使用缓存实现， 速度更快
    """
    # if n < 2:
    #     return n
    # return fibonacci(n-2) + fibonacci(n-1)
    return n if n < 2 else fibonacci(n-2) + fibonacci(n-1)


if __name__ == "__main__":
    print(fibonacci(6))


"""
运行结果：

$ python3 clockdeco_demo02.py
[0.00000024s] fibonacci(0) -> 0
[0.00000024s] fibonacci(1) -> 1
[0.00004101s] fibonacci(2) -> 1
[0.00000072s] fibonacci(3) -> 2
[0.00005102s] fibonacci(4) -> 3
[0.00000048s] fibonacci(5) -> 5
[0.00005960s] fibonacci(6) -> 8
8

"""
