"""
Component related classes.
"""
from cherapy.general.ComponentDB import *
from cherapy.general.Exceptions import *


class Element:

    def __init__(self, symbol, name, MW):
        self.symbol = symbol
        self.name = name
        self.MW = MW
        pass


class Component:

    def __init__(self, symbol=None, name=None, elements=None, comp=None):
        # a dictionary of containing elements and its value
        if comp is not None:
            self.elements = comp.elems
            self.symbol = comp.symbol
            self.name = comp.name
        else:
            self.elements = elements
            self.symbol = symbol
            self.name = name
        pass

    @classmethod
    def from_db(cls, symbol):
        l = [x for x in Components if x.symbol == symbol]
        if not l:
            raise ValueNotFoundException("cant find this value in the dictionary")
        el = l[0]
        new = cls(comp=el)
        return new


