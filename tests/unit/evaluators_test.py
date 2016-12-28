# -*- coding: utf-8; -*-
from pytest import fixture, raises
from thompson.bindings import Binding
from thompson.context import Context
from thompson.literals import BoolVal, NumberVal, StringVal, NullVal, NilConst
from thompson.builtin_operators import Pass
from thompson.evaluators import evaluate, find_evaluator
from thompson.evaluators import LiteralEvaluator, PassEvaluator


@fixture
def empty_context():
    return Context(Binding())


def test_find_evaluator(empty_context):
    assert isinstance(find_evaluator(empty_context, Pass()),
                      PassEvaluator)
    assert isinstance(find_evaluator(empty_context, BoolVal(True)),
                      LiteralEvaluator)
    assert isinstance(find_evaluator(empty_context, StringVal('')),
                      LiteralEvaluator)
    assert isinstance(find_evaluator(empty_context, NumberVal(42)),
                      LiteralEvaluator)
    assert isinstance(find_evaluator(empty_context, NullVal()),
                      LiteralEvaluator)
    with raises(ValueError):
        find_evaluator(empty_context, None)
    with raises(ValueError):
        find_evaluator(empty_context, 42)


def test_literals(empty_context):
    assert evaluate(empty_context, NullVal()) is NilConst
    assert evaluate(empty_context, BoolVal(True)) == BoolVal(True)
    assert evaluate(empty_context, BoolVal(False)) != BoolVal(True)
    assert evaluate(empty_context, StringVal('foo')) == StringVal('foo')
    assert evaluate(empty_context, StringVal('foo')) != StringVal('bar')
    assert evaluate(empty_context, NumberVal(42)) == NumberVal(42)
    assert evaluate(empty_context, NumberVal(3.14)) == NumberVal(3.14)


def test_pass(empty_context):
    assert evaluate(empty_context, Pass()) is NilConst
