# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod, abstractproperty
# TODO: понимание не глубокое, разобраться, слабо понятно предназначение
# и удобство от использования


class Car:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractproperty
    def speed(self):
        """get speed car"""
        pass

    @abstractmethod
    def move(self):
        """move car"""
        pass

# car = Car()


class Chevrolet(object):
    speed = 100

    def move(self):
        return "move with speed %s km/h" % self.speed

Car.register(Chevrolet)


chev = Chevrolet()
print(chev.move())
print(issubclass(Chevrolet, Car))
print(isinstance(chev, Car))