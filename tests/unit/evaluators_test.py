# -*- coding: utf-8; -*-
from pytest import fixture, raises
from thompson.bindings import Binding
from thompson.context import Context
from thompson.literals import BoolVal, NumberVal, StringVal, NullVal, NilConst
from thompson.builtin_operators import Pass
from thompson.builtin_operators import LogNot, LogOr, LogAnd
from thompson.evaluators import evaluate, find_evaluator
from thompson.evaluators import LiteralEvaluator, PassEvaluator


@fixture
def empty_context():
    return Context(Binding())


@fixture
def empty_context_eval(empty_context):
    return lambda n: evaluate(empty_context, n)


@fixture
def empty_context_find_evaluator(empty_context):
    return lambda n: find_evaluator(empty_context, n)


@fixture
def my_xor():
    """https://en.wikipedia.org/wiki/Exclusive_or"""
    return lambda a, b: LogAnd(LogOr(BoolVal(a), BoolVal(b)),
                               LogNot(LogAnd(BoolVal(a), BoolVal(b))))


def test_find_evaluator(empty_context_find_evaluator):
    F = empty_context_find_evaluator
    assert isinstance(F(Pass()), PassEvaluator)
    assert isinstance(F(BoolVal(True)), LiteralEvaluator)
    assert isinstance(F(StringVal('')), LiteralEvaluator)
    assert isinstance(F(NumberVal(42)), LiteralEvaluator)
    assert isinstance(F(NullVal()), LiteralEvaluator)
    with raises(ValueError):
        F(None)
    with raises(ValueError):
        F(42)


def test_literals(empty_context_eval):
    E = empty_context_eval
    assert E(NullVal()) is NilConst
    assert E(BoolVal(True)) == BoolVal(True)
    assert E(BoolVal(False)) != BoolVal(True)
    assert E(StringVal('foo')) == StringVal('foo')
    assert E(StringVal('foo')) != StringVal('bar')
    assert E(NumberVal(42)) == NumberVal(42)
    assert E(NumberVal(3.14)) == NumberVal(3.14)


def test_pass(empty_context_eval):
    assert empty_context_eval(Pass()) is NilConst


def test_log_ops(empty_context_eval, my_xor):
    E = empty_context_eval
    # Not.
    assert E(LogNot(BoolVal(False))) == BoolVal(True)
    assert E(LogNot(BoolVal(True))) == BoolVal(False)
    # And.
    assert E(LogAnd(BoolVal(True), BoolVal(True))) == BoolVal(True)
    assert E(LogAnd(BoolVal(True), BoolVal(False))) == BoolVal(False)
    assert E(LogAnd(BoolVal(False), BoolVal(True))) == BoolVal(False)
    assert E(LogAnd(BoolVal(False), BoolVal(False))) == BoolVal(False)
    # Or.
    assert E(LogOr(BoolVal(True), BoolVal(False))) == BoolVal(True)
    assert E(LogOr(BoolVal(False), BoolVal(True))) == BoolVal(True)
    assert E(LogOr(BoolVal(False), BoolVal(False))) == BoolVal(False)
    assert E(LogOr(BoolVal(True), BoolVal(True))) == BoolVal(True)
    # XOR = (a OR b) AND (NOT (a AND b))
    XOR = my_xor
    assert E(XOR(True, False)) == BoolVal(True)
    assert E(XOR(False, True)) == BoolVal(True)
    assert E(XOR(True, True)) == BoolVal(False)
    assert E(XOR(False, False)) == BoolVal(False)
