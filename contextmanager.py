# -*- coding: utf-8 -*-

from contextlib import contextmanager


# TODO: разобраться как это работает
@contextmanager
def tag(name):
    print "<%s>" % name
    yield
    print "</%s>" % name


with tag("h1"):
    print "foo"