# -*- coding: utf-8; *-
from sexpr import Atom


def test_atom():
    a1 = Atom('foo')
    assert a1 is not Atom('foo')
    assert a1 == Atom('foo')
    assert a1 != Atom('bar')
