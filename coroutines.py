# -*- coding: utf-8 -*-
def coroutine(fn):
    def init(*args, **kwargs):
        generator = fn(*args, **kwargs)
        generator.next()
        return generator
    return init


@coroutine
def receiver():
    print "send me message"
    while True:
        message = yield
        print("receiver message %s" % message)

r = receiver()
r.send("ky")
r.send("WARNING")