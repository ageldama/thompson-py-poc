# -*- coding: utf-8; -*-
from thompson.nodes.literals import NumberVal
from thompson.nodes.ops import ArithAdd, ArithSub
from thompson.nodes.ops import ArithMult, ArithMultMult
from thompson.nodes.ops import ArithDiv, ArithDivDiv, ArithRem


def test_arith_ops(empty_context_eval):
    E = empty_context_eval
    N = NumberVal
    # `+`
    assert E(ArithAdd(N(40), N(2))) == N(42)
    assert E(ArithAdd(N(40), N(2.1))) == N(42.1)
    # `-`
    assert E(ArithSub(N(45), N(3))) == N(42)
    assert E(ArithAdd(N(100),
                      ArithSub(N(42), N(100.0)))) == N(42.0)
    # `*`
    assert E(ArithMult(N(42), N(3))) == N(42 * 3)
    # `**`
    assert E(ArithMultMult(N(2), N(3))) == N(8)
    # `/`
    assert E(ArithDiv(N(7), N(2))) == N(3.5)
    # `//`
    assert E(ArithDivDiv(N(7), N(2))) == N(3)
    # `rem`
    assert E(ArithRem(N(7), N(2))) == N(1)
