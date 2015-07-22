# -*- coding: utf-8 -*-
import time


def my_decorator(fn):
    print u"я декоратор"

    def wrapper(q):
        print u"я обёртка с параметром %s" % q
        return fn(q)

    return wrapper


@my_decorator
def my_func(q=1):
    print u"я функция с параметром %s" % q

my_func(2)

# decorated_func = my_decorator(my_func)
# decorated_func(q=2)


def sleep_decorator(seconds):
    print "decorator with parameters"

    def decorator(fn):
        print "decorator body"

        def wrapper(*args):
            print "wrapper body"
            time.sleep(seconds)
            return fn(*args)

        return wrapper

    return decorator


@sleep_decorator(2)
def my_func2(q=1):
    print u"my_func2 with param %s" % q

my_func2(2)

# decorated_func = sleep_decorator(2)(my_func2)
# decorated_func(q=2)