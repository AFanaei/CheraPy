import unittest
from cherapy.general.Component import *
from cherapy.general.Exceptions import *


class ComponentsTest(unittest.TestCase):
    KNOWN_COMPS = {'CO2': 44, 'O2': 32, 'CH4': 16}

    def test_can_find(self):
        """
        should retrive a component from DB.
        """
        try:
            for i in self.KNOWN_COMPS.keys():
                comp = Component.from_db(i)
                self.assertEqual(comp.symbol, i)
        except ValueNotFoundException:
            print("value not found")

    def test_cant_find(self):
        """
        should create correct Exception.
        """
        self.assertRaises(ValueNotFoundException,Component.from_db, 'AHMADF')

    def test_MW(self):
        """
        should calculate mulecular weight correctly.
        """
        for k, v in self.KNOWN_COMPS.items():
            comp = Component.from_db(k)
            self.assertEqual(comp.MW, v)

if __name__ == '__main__':
    unittest.main()
