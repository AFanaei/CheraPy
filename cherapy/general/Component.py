"""
Component related classes.
"""
from .ComponentDB import *


class Element:

    def __init__(self, symbol, name, MW):
        self.symbol = symbol
        self.name = name
        self.MW = MW
        pass


class Component:

    def __init__(self, symbol, name, elements):
        # a dictionary of containing elements and its value
        self.elements = elements
        self.symbol = symbol
        self.name = name
        pass

    @classmethod
    def from_db(cls, symbol):
        el = [x for x in Elements if x.symbol == symbol][0]
        new = cls(el)
        return new


