# -*- coding: utf-8; -*-
from pytest import raises
from thompson.bindings import Binding
from thompson.context import Context
from thompson.literals import NumberVal, StringVal
from thompson.evaluators import evaluate
from thompson.builtin_operators import BindingRef
from thompson.builtin_operators import Assign, AssignGlobal, AssignUpvar


def test_simple_set_and_get():
    N, S = NumberVal, StringVal
    #
    binding = Binding()
    context = Context(binding)
    # assign.
    assert N(42) == evaluate(context, Assign('the-answer', N(42)))
    assert N(42) == evaluate(context, BindingRef(S('the-answer')))
    assert binding.get('the-answer') == N(42)
    # update.
    assert N(42.1) == evaluate(context, Assign(S('the-answer'), N(42.1)))
    assert N(42.1) == evaluate(context, BindingRef('the-answer'))
    assert binding.get('the-answer') == N(42.1)


def test_assign_global():
    N, S = NumberVal, StringVal
    #
    b_grandpa = Binding()
    b_papa = Binding(b_grandpa)
    b = Binding(b_papa)
    context = Context(b)
    # assign.
    assert N(42) == evaluate(context, AssignGlobal('the-answer', N(42)))
    assert N(42) == evaluate(context, BindingRef(S('the-answer')))
    with raises(NameError):
        assert b.get_no_inherits('the-answer') == N(42)
    with raises(NameError):
        assert b_papa.get_no_inherits('the-answer') == N(42)
    assert b_grandpa.get_no_inherits('the-answer') == N(42)


def test_assign_uplevel():
    N, S = NumberVal, StringVal
    #
    b_grandpa = Binding()
    b_papa = Binding(b_grandpa)
    b = Binding(b_papa)
    context = Context(b)
    # assign.
    assert N(42) == evaluate(context, AssignUpvar('the-answer', N(42)))
    assert N(42) == evaluate(context, BindingRef(S('the-answer')))
    with raises(NameError):
        assert b.get_no_inherits('the-answer') == N(42)
    with raises(NameError):
        assert b_grandpa.get_no_inherits('the-answer') == N(42)
    assert b_papa.get_no_inherits('the-answer') == N(42)
