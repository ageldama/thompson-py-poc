# -*- coding: utf-8; -*-
from thompson.bindings import Binding
from thompson.context import Context
from thompson.literals import NumberVal
from thompson.builtin_operators import Let, Assign, Const
from thompson.builtin_operators import BindingRef, ArithPlus
from thompson.evaluators import evaluate


def test_let():
    b = Binding()
    c = Context(b)
    N = NumberVal
    let_expr = Let([Const('x', N(2)), Assign('y', N(1))],
                   ArithPlus(BindingRef('x'), BindingRef('y')))
    result = evaluate(c, let_expr)
    assert result == N(3)
    assert not b.contains('x')
    assert not b.contains('y')
