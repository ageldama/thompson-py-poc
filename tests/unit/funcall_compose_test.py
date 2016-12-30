# -*- coding: utf-8; -*-
from thompson.bindings import Binding
from thompson.context import Context
from thompson.nodes.literals import NumberVal
from thompson.nodes.literals import FunctionParamVal, FunctionVal
from thompson.nodes.ops import Assign
from thompson.nodes.ops import Funcall
from thompson.nodes.ops import ArithAdd, ArithMult, BindingRef
from thompson.evaluators import evaluate


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
    body = ArithAdd(N(1), BindingRef('x'))
    return evaluate(c, Assign('inc1', FunctionVal(params, body)))


def define_square(c):
    params = [FunctionParamVal('x')]
    body = ArithMult(BindingRef('x'), BindingRef('x'))
    return evaluate(c, Assign('square', FunctionVal(params, body)))


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
    # compose(square, inc1) ==> square(inc1(x))
    evaluate(c_root, Assign('my_fun',
                            Funcall(BindingRef('compose1'),
                                    [BindingRef('square'),
                                     BindingRef('inc1')])))
    evaluate(c_root, BindingRef('my_fun'))
    # test it.
    result = evaluate(c_root, Funcall(BindingRef('my_fun'), [N(2)]))
    assert result == N(9)
