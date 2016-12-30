# -*- coding: utf-8; -*-
from thompson.context import Context, Binding
from thompson.evaluators import evaluate
from thompson.nodes.literals import NumberVal, NilConst
from thompson.nodes.ops import Prog1, ProgN, ParProg
from thompson.nodes.ops import Assign, BindingRef, ArithAdd


def test_prog1():
    N = NumberVal
    #
    b = Binding()
    c = Context(b)
    #
    l = Prog1([Assign('a', N(1)),
               Assign('b', ArithAdd(N(1), BindingRef('a'))),
               Assign('c', ArithAdd(N(1), BindingRef('b')))])
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
               Assign('b', ArithAdd(N(1), BindingRef('a'))),
               Assign('c', ArithAdd(N(1), BindingRef('b')))])
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
