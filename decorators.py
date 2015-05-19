# -*- coding: utf-8 -*-


def my_decorator(fn):
    print u"я декоратор с параметром %s"

    def wrapper(q):
        print u"я обёртка с параметром %s" % q
        return fn(q)

    return wrapper


@my_decorator
def my_func(q=1):
    print u"я функция с параметром %s" % q

# decorated_func = my_decorator(my_func)
# decorated_func(q=2)

my_func(2)