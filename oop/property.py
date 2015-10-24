# -*- coding: utf-8 -*-


class Circle(object):
    def __init__(self):
        self.radius = None
        self.diameter = None

    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0