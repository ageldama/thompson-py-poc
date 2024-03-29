# -*- coding: utf-8; -*-
import thompson.evaluators.registry  # noqa: F401
from thompson.nodes.literals import NumberVal, BoolVal
from thompson.nodes.ops import ComparLt, ComparGt, ComparLe, ComparGe


def test_compar_ops(empty_context_eval):
    E = empty_context_eval
    N = NumberVal
    B = BoolVal
    # lt.
    assert E(ComparLt([N(42), N(4000)])) == B(True)
    assert E(ComparLt([N(42.0), N(4000)])) == B(True)
    # le.
    assert E(ComparLe([N(42), N(4000)])) == B(True)
    assert E(ComparLe([N(42), N(42.0)])) == B(True)
    # gt.
    assert E(ComparGt([N(42), N(4000)])) == B(False)
    assert E(ComparGt([N(42), N(42.0)])) == B(False)
    assert E(ComparGt([N(42), N(-4000)])) == B(True)
    # ge.
    assert E(ComparGe([N(42), N(-4000)])) == B(True)
    assert E(ComparGe([N(42), N(42.0)])) == B(True)
    assert E(ComparGe([N(42), N(420)])) == B(False)
