# -*- coding: utf-8; -*-
from pytest import fixture
import thompson.evaluators.registry  # noqa: F401
from thompson.nodes.literals import BoolVal
from thompson.nodes.ops import LogNot, LogOr, LogAnd


@fixture
def my_xor():
    """https://en.wikipedia.org/wiki/Exclusive_or"""
    return lambda a, b: LogAnd([LogOr([BoolVal(a), BoolVal(b)]),
                                LogNot(LogAnd([BoolVal(a), BoolVal(b)]))])


def test_log_ops(empty_context_eval, my_xor):
    E = empty_context_eval
    B = BoolVal
    # Not.
    assert E(LogNot(B(False))) == B(True)
    assert E(LogNot(B(True))) == B(False)
    # And.
    assert E(LogAnd([B(True), B(True)])) == B(True)
    assert E(LogAnd([B(True), B(False)])) == B(False)
    assert E(LogAnd([B(False), B(True)])) == B(False)
    assert E(LogAnd([B(False), B(False)])) == B(False)
    # Or.
    assert E(LogOr([B(True), B(False)])) == B(True)
    assert E(LogOr([B(False), B(True)])) == B(True)
    assert E(LogOr([B(False), B(False)])) == B(False)
    assert E(LogOr([B(True), B(True)])) == B(True)
    # XOR = (a OR b) AND (NOT (a AND b))
    XOR = my_xor
    assert E(XOR(True, False)) == B(True)
    assert E(XOR(False, True)) == B(True)
    assert E(XOR(True, True)) == B(False)
    assert E(XOR(False, False)) == B(False)
