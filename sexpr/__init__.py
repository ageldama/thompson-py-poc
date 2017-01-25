# -*- coding: utf-8; -*-
class Atom(object):
    def __init__(self, val):
        self.val = val

    def __hash__(self):
        return hash((self.val))

    def __str__(self):
        return "Atom('{}')".format(self.val)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if other is None:
            return False
        elif isinstance(other, Atom):
            return other.val == self.val
        else:
            return False


class Exprs(list):
    pass


def dumps(obj) -> str:
    return ""  # TODO:
