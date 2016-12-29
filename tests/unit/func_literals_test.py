# -*- coding: utf-8; -*-
from thompson.bindings import Binding
from thompson.context import Context
from thompson.literals import NumberVal, NilConst, StringVal
from thompson.literals import FunctionParamVal
from thompson.evaluators import evaluate
from thompson.evaluators import gimme_str_anyway
import pytest


def test_gimme_str():
    b = Binding()
    c = Context(b)
    S = StringVal
    #
    assert gimme_str_anyway(c, S('foo')) == 'foo'
    assert gimme_str_anyway(c, 'foo') == 'foo'


def test_func_param_eval():
    b = Binding()
    c = Context(b)
    S = StringVal
    r1 = evaluate(c, FunctionParamVal(S('foo')))
    assert r1.name == 'foo'
    assert isinstance(r1.name, str)
    r2 = evaluate(c, FunctionParamVal('foo'))
    assert isinstance(r2.name, str)
    assert r1.name == r2.name


def test_func_literal_eval():
    pass
