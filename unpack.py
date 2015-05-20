# -*- coding: utf-8 -*-
my_typle = (1, 2, 3)
my_dict = {'a': 1, 'b': 2}


def args_sum(*args):
    summary = 0
    for x in args:
        summary += x

    return summary

print args_sum(*my_typle)