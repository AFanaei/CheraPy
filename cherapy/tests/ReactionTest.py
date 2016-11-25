import unittest

from cherapy.general import Component, ValueNotFoundException, NotInMassBalanceException
from cherapy.reaction.ReactionBase import ReactionBase


class ComponentsTest(unittest.TestCase):

    def test_reaction_in_balance(self):
        """
        should work for ok reaction.
        """
        class Reaction(ReactionBase):
            def __init__(self):
                super(Reaction, self).__init__()
                self.comps = {'CH4': -1, 'O2': -2, 'CO2': 1, 'H2O': 2}

        r = Reaction()

    def test_reaction_not_balance(self):
        """
        should generate exception there is no mass balance
        """
        class Reaction(ReactionBase):
            def __init__(self):
                super(Reaction, self).__init__()
                self.comps = {'CH4': -1, 'O2': .5}

        self.assertRaises(NotInMassBalanceException, Reaction)

if __name__ == '__main__':
    unittest.main()
