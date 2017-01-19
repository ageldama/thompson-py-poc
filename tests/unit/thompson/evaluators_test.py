# -*- coding: utf-8; -*-
from pytest import fixture, raises
from thompson.nodes.literals import BoolVal, NumberVal, StringVal
from thompson.nodes.literals import NullVal, NilConst
from thompson.nodes.ops import Pass
from thompson.evaluators import find_evaluator
from thompson.evaluators import LiteralEvaluator, PassEvaluator


@fixture
def empty_context_find_evaluator(empty_context):
    return lambda n: find_evaluator(empty_context, n)


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
