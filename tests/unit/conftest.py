# -*- coding: utf-8; -*-
from pytest import fixture
from thompson.context import Context, Binding
from thompson.evaluators import evaluate
from typing import Callable


@fixture(scope='function')
def empty_context() -> 'Context':
    return Context(Binding())


@fixture(scope='function')
def empty_context_eval(empty_context: 'Context') -> Callable:
    return lambda n: evaluate(empty_context, n)
