# -*- coding: utf-8; -*-


class Atom(object):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return "Atom[{}]".format(self.val)

    def __eq__(self, other):
        if isinstance(other, Atom):
            return other.val == self.val
        else:
            return False


def parse_file(f):
    return None  # TODO:
