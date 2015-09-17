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


def sleep_decorator(*decorator_args, **decorator_kwargs):
    print "decorator sleep with parameters"

    def decorator(function):
        print "decorator body"

        def wrapper(*func_args, **func_kwargs):
            print "wrapper body"
            seconds = 1
            time.sleep(seconds)
            return function(*func_args)

        return wrapper

    return decorator


@sleep_decorator()
def my_func2(q=1):
    print u"my_func2 with param %s" % q

my_func2(5)

# decorated_func = sleep_decorator(my_func2)
# decorated_func()