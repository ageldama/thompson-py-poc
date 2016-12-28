# -*- coding: utf-8; -*-
from thompson.bindings import Binding
from thompson.context import Context
from thompson.literals import NumberVal, NilConst, StringVal
from thompson.evaluators import evaluate
from thompson.builtin_operators import ComparLt
from thompson.builtin_operators import CondElse, CondItem
from thompson.builtin_operators import CaseElse, CaseItem
from thompson.builtin_operators import Assign


def test_cond_else():
    N, S = NumberVal, StringVal
    b = Binding()
    c = Context(b)
    #
    expr = Assign("x", CondElse([CondItem(ComparLt(N(1), N(-1)), S("foo")),
                                 CondItem(ComparLt(N(1), N(42)), S("bar"))],
                                S("zoo")))
    result = evaluate(c, expr)
    assert result == S("bar")
    assert b.get("x") == S("bar")
    #
    expr = Assign("y", CondElse([CondItem(ComparLt(N(1), N(-1)), S("foo")),
                                 CondItem(ComparLt(N(1), N(-42)), S("bar"))],
                                S("zoo")))
    result = evaluate(c, expr)
    assert result == S('zoo')
    assert S('zoo') == b.get('y')


def test_cond_only():
    N, S = NumberVal, StringVal
    b = Binding()
    c = Context(b)
    #
    expr = Assign("x", CondElse([CondItem(ComparLt(N(1), N(-1)), S("foo")),
                                 CondItem(ComparLt(N(1), N(42)), S("bar"))]))
    result = evaluate(c, expr)
    assert result == S("bar")
    assert b.get("x") == S("bar")
    #
    expr = Assign("y", CondElse([CondItem(ComparLt(N(1), N(-1)), S("foo")),
                                 CondItem(ComparLt(N(1), N(-42)), S("bar"))]))
    result = evaluate(c, expr)
    assert result == NilConst
    assert NilConst == b.get('y')


def test_case_else():
    N, S = NumberVal, StringVal
    b = Binding()
    c = Context(b)
    #
    expr = Assign("x", CaseElse(N(2),
                                [CaseItem(N(1), S("foo")),
                                 CaseItem(N(2), S("bar"))],
                                S("zoo")))
    result = evaluate(c, expr)
    assert result == S("bar")
    assert b.get("x") == S("bar")
    #
    expr = Assign("y", CaseElse(N(999),
                                [CaseItem(N(1), S("foo")),
                                 CaseItem(N(2), S("bar"))],
                                S("zoo")))
    result = evaluate(c, expr)
    assert result == S("zoo")
    assert b.get("y") == S("zoo")


def test_case_only():
    N, S = NumberVal, StringVal
    b = Binding()
    c = Context(b)
    #
    expr = Assign("x", CaseElse(N(2),
                                [CaseItem(N(1), S("foo")),
                                 CaseItem(N(2), S("bar"))]))
    result = evaluate(c, expr)
    assert result == S("bar")
    assert b.get("x") == S("bar")
    #
    expr = Assign("y", CaseElse(N(999),
                                [CaseItem(N(1), S("foo")),
                                 CaseItem(N(2), S("bar"))]))
    result = evaluate(c, expr)
    assert result == NilConst
    assert NilConst == b.get('y')