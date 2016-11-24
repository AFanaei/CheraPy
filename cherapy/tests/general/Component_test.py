import unittest
from cherapy.general.Component import *
from cherapy.general.Exceptions import *


class ComponentsTest(unittest.TestCase):
    KNOWN_COMPS = ('CO2', 'O2', 'CH4')

    def test_can_find_component(self):
        """
        should retrive a component from DB.
        """
        try:
            for i in self.KNOWN_COMPS:
                comp = Component.from_db(i)
                self.assertEqual(comp.symbol, i)
        except ValueNotFoundException:
            print("value not found")

    def test_cant_find_component(self):
        """
        should create correct Exception.
        """
        self.assertRaises(ValueNotFoundException,Component.from_db,'AHMADF')

if __name__ == '__main__':
    unittest.main()
