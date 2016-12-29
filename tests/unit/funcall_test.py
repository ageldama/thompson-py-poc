# -*- coding: utf-8; -*-
from thompson.bindings import Binding
from thompson.context import Context
from thompson.literals import StringVal, NumberVal
from thompson.literals import FunctionParamVal, FunctionVal
from thompson.builtin_operators import Assign, AssignGlobal, AssignUpvar
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


def test_closure1_inc():
    N = NumberVal
    b_root = Binding()
    # set inc = fun {|x| ... }
    b_creation = Binding(b_root)
    b_creation.set('magic', N(42))
    c_creation = Context(b_creation)
    params_expr = [FunctionParamVal('x')]
    body_expr = ArithPlus(BindingRef('x'), BindingRef('magic'))
    evaluate(c_creation,
             AssignGlobal('inc', FunctionVal(params_expr, body_expr)))
    # funcall inc(1).
    b2 = Binding(b_root)
    c2 = Context(b2)
    result = evaluate(c2, Funcall(BindingRef('inc'), [N(1)]))
    #
    assert result == N(43)
    assert b_root.contains_no_inherits('inc')
    assert not b_root.contains_no_inherits('magic')
    assert not b2.contains_no_inherits('inc')
    assert not b_creation.contains_no_inherits('inc')


def test_closure2_counter():
    N = NumberVal
    b_root = Binding()
    # set counter = fun {|x| ... }
    b_creation = Binding(b_root)
    b_creation.set('count', N(0))
    c_creation = Context(b_creation)
    params_expr = []
    # NOTE: Use `AssignUpvar` to modify closure's binding, not
    # `Assign`. Because, basically, function's closure is wrapped with
    # another `Binding` to separate function's own scope.
    body_expr = AssignUpvar('count', ArithPlus(N(1), BindingRef('count')))
    evaluate(c_creation,
             AssignGlobal('counter', FunctionVal(params_expr, body_expr)))
    #
    b2 = Binding(b_root)
    c2 = Context(b2)
    for i in range(3):
        result = evaluate(c2, Funcall(BindingRef('counter'), []))
        assert result == N(i+1)
    #
    assert not b2.contains_no_inherits('count')
    assert not b_root.contains_no_inherits('count')
    assert b_creation.contains_no_inherits('count')
    print(b_creation.get('count'))
    assert b_creation.get('count') == N(3)


def test_make_adder():
    S, N = StringVal, NumberVal
    b = Binding()
    c = Context(b)
    # set adder = fun {|x, y| ... }
    params_expr = [FunctionParamVal(S('x')), FunctionParamVal('y')]
    body_expr = ArithPlus(BindingRef('x'), BindingRef('y'))
    evaluate(c, Assign('adder', FunctionVal(params_expr, body_expr)))
    # execute.
    result = evaluate(c, Funcall(BindingRef('adder'), [N(1), N(6)]))
    assert result == N(7)


def test_func_composition():
    pass
