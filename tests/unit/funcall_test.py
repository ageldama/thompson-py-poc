# -*- coding: utf-8; -*-
from thompson.bindings import Binding
from thompson.context import Context
from thompson.literals import StringVal, NumberVal
from thompson.literals import FunctionParamVal, FunctionVal
from thompson.builtin_operators import Assign, AssignGlobal, AssignUpvar
from thompson.builtin_operators import Funcall
from thompson.builtin_operators import ArithPlus, ArithMult, BindingRef
from thompson.evaluators import evaluate
import pytest


def test_simple_adder():
    """A function can take parameters and evaluates to a value."""
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
    """A function has a closure, a binding.
    And can access to its variables."""
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
    """A function can (re)assign variables in a closure with `AssignUpvar`."""
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
    """A function can be referenced as a variable."""
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


def define_make_incx(c):
    params_expr = [FunctionParamVal('x')]
    body = FunctionVal([FunctionParamVal('n')],
                       ArithPlus(BindingRef('x'), BindingRef('n')))
    return evaluate(c, Assign('make_incx', FunctionVal(params_expr, body)))


def test_incx():
    N = NumberVal
    b = Binding()
    c = Context(b)
    #
    define_make_incx(c)
    evaluate(c, Assign('inc42', Funcall(BindingRef('make_incx'), [N(42)])))
    #
    result = evaluate(c, Funcall(BindingRef('inc42'), [N(1)]))
    assert result == N(43)


def define_compose1(c):
    """compose two 1-arity functions into a function."""
    params_expr = [FunctionParamVal('g'), FunctionParamVal('f')]
    body = FunctionVal([FunctionParamVal('x')],
                       Funcall(BindingRef('g'),
                               [Funcall(BindingRef('f'), [BindingRef('x')])]))
    return evaluate(c, Assign('compose1', FunctionVal(params_expr, body)))


def define_inc1(c):
    N = NumberVal
    params = [FunctionParamVal('x')]
    body = ArithPlus(N(1), BindingRef('x'))
    return evaluate(c, Assign('inc1', FunctionVal(params, body)))


def define_square(c):
    params = [FunctionParamVal('x')]
    body = ArithMult(BindingRef('x'), BindingRef('x'))
    return evaluate(c, Assign('square', FunctionVal(params, body)))


@pytest.mark.skip
def test_func_composition():
    """Test on function-value as return-value and parameter to another
    function."""
    N = NumberVal
    b_root = Binding()
    c_root = Context(b_root)
    # funcs.
    define_compose1(c_root)
    define_inc1(c_root)
    assert evaluate(c_root, Funcall(BindingRef('inc1'), [N(1)])) == N(2)
    define_square(c_root)
    assert evaluate(c_root, Funcall(BindingRef('square'), [N(4)])) == N(16)
    # compose - square(inc1(x))
    evaluate(c_root, Assign('my_fun',
                            Funcall(BindingRef('compose1'),
                                    [BindingRef('square'),
                                     BindingRef('inc1')])))
    evaluate(c_root, BindingRef('my_fun'))
    # test it.
    # TODO: FIXME:
    result = evaluate(c_root, Funcall(BindingRef('my_fun'), [N(2)]))
    assert result == N(9)