from collections import namedtuple

__all__ = ('Elements', 'Components')

Elem = namedtuple('Elem', ['symbol', 'name', 'MW'], verbose=True)
Comp = namedtuple('Comp', ['symbol', 'name', 'elems'], verbose=True)

Elements = {
    'c': Elem('c', 'Carbon', 12),
    'h': Elem('h', 'Hydrogen', 1),
    'o': Elem('o', 'Oxygen', 16),
}

Components = [
    Elem('ch4', 'methane', {Elements['c']:1, Elements['h']:4}),
    Elem('h2', 'hydrogen', {Elements['h']:2}),
    Elem('co2', 'carbon dioxide', {Elements['c']:1, Elements['o']:2}),
    Elem('co', 'carbon monoxide', {Elements['c']:1, Elements['o']:1}),
]

