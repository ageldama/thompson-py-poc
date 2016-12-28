# -*- coding: utf-8; -*-
from pytest import fixture
from thompson.bindings import Binding
from thompson.context import Context
from thompson.evaluators import evaluate


@fixture
def empty_context():
    return Context(Binding())


@fixture
def empty_context_eval(empty_context):
    return lambda n: evaluate(empty_context, n)
