# -*- coding: utf-8 -*-

a = 1


def my_func(q=None):
    global a
    a = 2
    return a, 1


def fn(q, b):
    print q + b

fn(*my_func())