# -*- coding: utf-8 -*-
def sum_args_functional(*args):
    total = lambda x, y: x + y
    return reduce(total, args)


def sum_args_classic(*args):
    x = 0
    for x in args:
        x += x
    return x


def sum_args_rec(*args):
    return args[0] + sum_args_rec(*args[1:]) if len(args) > 1 else args[0]