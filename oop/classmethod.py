# -*- coding: utf-8 -*-

import math


class Circle(object):
    def __init__(self, radius):
        self.radius = radius
        print self.__class__

    def area(self):
        return math.pi * self.radius ** 2.0

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)


class Wheel(Circle):
    def perimeter(self):
        return 2.0 * math.pi * self.radius