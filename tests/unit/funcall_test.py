# -*- coding: utf-8; -*-
from thompson.bindings import Binding
from thompson.context import Context
from thompson.literals import StringVal, NumberVal
from thompson.literals import FunctionParamVal, FunctionVal
from thompson.builtin_operators import Funcall
from thompson.builtin_operators import ArithPlus, BindingRef
from thompson.evaluators import evaluate


def test_simple_adder():
    S, N = StringVal, NumberVal
    b = Binding()
    b.set('x', 42)
    b.set('y', 123)
    c = Context(b)
    params_expr = [FunctionParamVal(S('x')), FunctionParamVal('y')]
    body_expr = ArithPlus(BindingRef('x'), BindingRef('y'))
    fun_expr = FunctionVal(params_expr, body_expr)
    funcall_expr = Funcall(fun_expr, [N(1), N(2)])
    #
    result = evaluate(c, funcall_expr)
    assert result == N(3)
    assert fun_expr.binding.get('x') == N(1)  # Not a good behaviors.
    assert fun_expr.binding.get('y') == N(2)


def test_closure1():
    # TODO: can ref to creation-context?
    # TODO: cannot ref with eval-context?
    pass


def test_make_adder():
    pass


def test_func_composition():
    pass


def test_func_var():
    pass
