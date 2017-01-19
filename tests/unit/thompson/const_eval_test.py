# -*- coding: utf-8; -*-
from thompson.nodes.literals import NumberVal
from thompson.nodes.ops import Const, Assign
from pytest import raises


def test_const(empty_context_eval):
    E = empty_context_eval
    N = NumberVal
    result = E(Const('pi', N(3.14)))
    assert result == N(3.14)
    #
    E(Assign('x', N(0)))
    E(Const('x', N(777)))
    with raises(KeyError):
        E(Assign('x', N(0)))
    with raises(KeyError):
        E(Const('x', N(0)))
