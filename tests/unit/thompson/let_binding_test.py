# -*- coding: utf-8; -*-
from thompson.context import Context, Binding
from thompson.nodes.literals import NumberVal
from thompson.nodes.ops import Let, Assign, Const
from thompson.nodes.ops import BindingRef, ArithAdd
from thompson.evaluators import evaluate


def test_let():
    b = Binding()
    c = Context(b)
    N = NumberVal
    let_expr = Let([Const('x', N(2)), Assign('y', N(1))],
                   ArithAdd(BindingRef('x'), BindingRef('y')))
    result = evaluate(c, let_expr)
    assert result == N(3)
    assert not b.contains('x')
    assert not b.contains('y')
