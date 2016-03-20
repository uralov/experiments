# -*- coding: utf-8 -*-

import time


def timer(fn):
    def wrapper():
        start = time.time()
        fn()
        end = time.time()
        print "function '{0}' is executed {1} seconds".format(fn.__name__,
                                                              end - start)
    return wrapper


@timer
def main():
    for i in xrange(10**8):
        pass

main()


start = time.time()
for i in xrange(10**8):
    pass
end = time.time()
print "code is executed {0} seconds".format(end - start)
