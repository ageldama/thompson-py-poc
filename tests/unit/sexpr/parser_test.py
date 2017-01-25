# -*- coding: utf-8; -*-
from sexpr import Atom
from sexpr.parser import parser


def test_parser():
    assert parser is not None


def test_simplest_atom():
    P = parser.parse
    assert P("1234") == 1234
    assert P('"foobar"') == "foobar"
    assert P('atom') == Atom("atom")
    assert P('(atom)') == [Atom("atom")]
    assert P('(atom "foo" 42)') == [Atom("atom"), "foo", 42]
    assert P('()') == []
    assert P('(())') == [[]]
    assert P('(() ())') == [[], []]
    assert P('(() (() abc))') == [[], [[], Atom('abc')]]
    assert P('(atom "foo" (abc def ()) 42)') == [Atom("atom"), "foo",
                                                 [Atom("abc"),
                                                  Atom("def"),
                                                  []],
                                                 42]
