#!/usr/bin/env python 
# coding:utf-8
# @Time :8/21/18 12:00

import time
import logging
from functools import wraps


def run_time(logger=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            # logger.info("{} 程序运行了 {} s".format(func.__name__, "%s" % round(end_time - start_time, 2)))
            print ("{} 程序运行了 {} s".format(func.__name__, "%s" % round(end_time - start_time, 2)))
        return wrapper
    return decorator


if __name__ == '__main__':
    logging.basicConfig()
    logger = logging.getLogger('demo')

    @run_time(logger)
    def demo():
        for i in range(10000000):
            pass
    demo()
