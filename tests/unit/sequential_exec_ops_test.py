# -*- coding: utf-8; -*-
from thompson.bindings import Binding
from thompson.context import Context
from thompson.literals import NumberVal, NilConst
from thompson.evaluators import evaluate
from thompson.builtin_operators import Prog1, ProgN, ParProg
from thompson.builtin_operators import Assign, BindingRef, ArithPlus


def test_prog1():
    N = NumberVal
    #
    b = Binding()
    c = Context(b)
    #
    l = Prog1([Assign('a', N(1)),
               Assign('b', ArithPlus(N(1), BindingRef('a'))),
               Assign('c', ArithPlus(N(1), BindingRef('b')))])
    result = evaluate(c, l)
    assert result == N(1)
    assert evaluate(c, BindingRef('a')) == N(1)
    assert evaluate(c, BindingRef('b')) == N(2)
    assert evaluate(c, BindingRef('c')) == N(3)


def test_progn():
    N = NumberVal
    #
    b = Binding()
    c = Context(b)
    #
    l = ProgN([Assign('a', N(1)),
               Assign('b', ArithPlus(N(1), BindingRef('a'))),
               Assign('c', ArithPlus(N(1), BindingRef('b')))])
    result = evaluate(c, l)
    assert result == N(3)
    assert evaluate(c, BindingRef('a')) == N(1)
    assert evaluate(c, BindingRef('b')) == N(2)
    assert evaluate(c, BindingRef('c')) == N(3)


def test_parprog():
    N = NumberVal
    #
    b = Binding()
    c = Context(b)
    #
    l = ParProg([Assign('a', N(1)),
                 Assign('b', N(2))])
    result = evaluate(c, l)
    assert result == NilConst
    assert evaluate(c, BindingRef('a')) == N(1)
    assert evaluate(c, BindingRef('b')) == N(2)
