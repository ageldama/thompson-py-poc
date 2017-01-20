# -*- coding: utf-8; -*-
from sexpr import Atom


def test_atom_eq():
    assert Atom('foo') == Atom('FOO'.lower())


def test_atom_hashability():
    h = {}
    h[Atom('foo')] = 'bar'
    h[Atom('42')] = 'spameggs'
    assert Atom('foo') in h
    assert Atom('42') in h
    assert Atom('bacon') not in h
    assert h[Atom('42')] == 'spameggs'
