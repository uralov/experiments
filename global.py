# -*- coding: utf-8 -*-
a = 1


def foo():
    global a
    a = 2


def bar():
    a = 3

foo()
bar()
print(a)