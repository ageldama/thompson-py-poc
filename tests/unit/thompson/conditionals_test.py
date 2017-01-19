# -*- coding: utf-8; -*-
from thompson.context import Context, Binding
from thompson.evaluators import evaluate
from thompson.nodes.literals import NumberVal, NilConst, BoolVal
from thompson.nodes.ops import ComparLt
from thompson.nodes.ops import IfThenElse, When, Unless
from thompson.nodes.ops import Assign


def test_if_then():
    N = NumberVal
    b = Binding()
    c = Context(b)
    result = evaluate(c, IfThenElse(ComparLt(N(3), N(42)),
                                    Assign('a', N(777))))  # Jackpot!
    assert N(777) == result
    assert N(777) == b.get('a')


def test_if_then_else1():
    N = NumberVal
    b = Binding()
    c = Context(b)
    #
    result = evaluate(c, IfThenElse(ComparLt(N(3), N(42)),
                                    Assign('a', N(777)),
                                    Assign('b', N(12))))
    assert N(777) == result
    assert N(777) == b.get('a')
    assert not b.contains('b')


def test_if_then_else2():
    N = NumberVal
    b = Binding()
    c = Context(b)
    #
    result = evaluate(c, IfThenElse(ComparLt(N(333), N(42)),
                                    Assign('a', N(777)),
                                    Assign('b', N(12))))
    assert N(12) == result
    assert N(12) == b.get('b')
    assert not b.contains('a')


def test_when():
    N = NumberVal
    b = Binding()
    c = Context(b)
    #
    result = evaluate(c, When(ComparLt(N(3), N(42)),
                              Assign('a', N(777))))  # Jackpot!
    assert N(777) == result
    assert N(777) == b.get('a')
    #
    result = evaluate(c, When(ComparLt(N(3333), N(42)),
                              Assign('b', N(777))))
    assert NilConst == result
    assert not b.contains('b')


def test_unless():
    N = NumberVal
    b = Binding()
    c = Context(b)
    #
    result = evaluate(c, Unless(ComparLt(N(3333), N(42)),
                                Assign('a', N(777))))  # Jackpot!
    assert N(777) == result
    assert N(777) == b.get('a')


def test_unless2():
    N = NumberVal
    b = Binding()
    c = Context(b)
    result = evaluate(c, Unless(ComparLt(N(42), N(3333)),
                                Assign('b', N(777))))
    assert NilConst == result
    assert not b.contains('b')


def test_unless3():
    B, N = BoolVal, NumberVal
    b = Binding()
    c = Context(b)
    result = evaluate(c, Unless(B(True), Assign('b', N(777))))
    assert NilConst == result
    assert not b.contains('b')
