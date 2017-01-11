# -*- coding: utf-8; -*-
from pytest import fixture
from thompson.context import Context, Binding
from thompson.evaluators import evaluate
from typing import Callable
from pathlib import Path


@fixture(scope='function')
def empty_context() -> 'Context':
    return Context(Binding())


@fixture(scope='function')
def empty_context_eval(empty_context: 'Context') -> Callable:
    return lambda n: evaluate(empty_context, n)


@fixture
def test_data_path():
    return (Path(__file__).parent.parent / 'data')
