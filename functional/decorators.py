# -*- coding: utf-8 -*-
import time


def sleep_3_decorator(fn):
    print u"я декоратор"

    def wrapper(q):
        time.sleep(3)
        return fn(q)

    return wrapper


@sleep_3_decorator
def my_func(q):
    print u"я функция с параметром %s" % q

my_func(2)

# decorated_func = sleep_3_decorator(my_func)
# decorated_func(q=2)


def sleep_decorator(sleep_time):
    def decorator(function):
        def wrapper(*func_args, **func_kwargs):
            print "wrapper body"
            time.sleep(sleep_time)
            return function(*func_args, **func_kwargs)

        return wrapper

    return decorator


@sleep_decorator(2)
def my_func2(q):
    print u"my_func2 with param %s" % q

my_func2(5)

# decorated_func = sleep_decorator(my_func2)
# decorated_func()