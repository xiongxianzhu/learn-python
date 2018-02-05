#coding: utf-8

"""
    定义一个装饰器用于计算程序运行时间并使用它。
"""

import time
from functools import wraps

def calc_run_time(func):

    @wraps(func)
    def func_timer(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("running time: %s seconds." % str(end-start))

    return func_timer


@calc_run_time
def go():
    for i in xrange(100):
        print i

if __name__ == "__main__":
    go()