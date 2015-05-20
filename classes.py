# -*- coding: utf-8 -*-

a = 5


class Ancestor(object):
    __b = 1

    def abc(self):
        print('abc method')
        print a
        print self.__b


class Descendant(Ancestor):
    def abc(self):
        print('qqq method')

d = Ancestor()
d.abc()