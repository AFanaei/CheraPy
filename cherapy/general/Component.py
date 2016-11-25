"""
Component related classes.
"""
from cherapy.general.ComponentDB import *
from cherapy.general.Exceptions import *


class Element:

    def __init__(self, symbol=None, name=None, MW=None, elem=None):
        if elem is not None:
            self.symbol = elem.symbol
            self.name = elem.name
            self.MW = elem.MW
        else:
            self.symbol = symbol
            self.name = name
            self.MW = MW
        pass

    @classmethod
    def from_db(cls, symbol):
        l = [x for x in Elements if x.symbol == symbol]
        if not l:
            raise ValueNotFoundException("cant find this value in the dictionary")
        el = l[0]
        new = cls(elem=el)
        return new


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
            raise ValueNotFoundException("cant find {} value in the dictionary".format(symbol))
        el = l[0]
        new = cls(comp=el)
        return new

    @property
    def MW(self):
        sumy = 0
        for k, v in self.elements.items():
            elem = Element.from_db(k)
            sumy += elem.MW*v
        return sumy


