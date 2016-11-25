from cherapy.general import Component, NotInMassBalanceException, Element
from collections import defaultdict


class ReactionMeta(type):
    def __call__(cls, *args, **kwargs):
        """Called when you call MyNewClass() """
        obj = type.__call__(cls, *args, **kwargs)
        obj.after_init()
        return obj


class ReactionBase(metaclass=ReactionMeta):
    def __init__(self):
        self.comps={}
        self.compDict={}
        pass

    def after_init(self):
        self.get_comps()
        self.is_valid()

    def is_valid(self):
        overal_mass = 0
        elems_mass = defaultdict(int)
        for k, v in self.comps.items():
            overal_mass += self.compDict[k].MW*v
            elems = self.compDict[k].elements
            for el, n in elems.items():
                elemd = Element.from_db(el)
                elems_mass[el] += v*elemd.MW*n
        if abs(overal_mass) > 0.01:
            raise NotInMassBalanceException("overall mass balance failed.")
        for k, v in elems_mass.items():
            print("{}:{} ".format(k, v))
            if abs(v) > 0.01:
                raise NotInMassBalanceException("component {} not in mass balance".format(k))

    def get_comps(self):
        for k in self.comps.keys():
            self.compDict[k] = Component.from_db(k)


# class Reaction(ReactionBase):
#     def __init__(self):
#         super(Reaction, self).__init__()
#         self.comps = {'CH4': -1, 'O2': -2, 'CO2': 1, 'H2O': 2}
