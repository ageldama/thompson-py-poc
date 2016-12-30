# -*- coding: utf-8; -*-
from thompson.nodes.literals import StringVal, NumberVal, BoolVal, NilConst
from thompson.nodes.literals import MappedVal, MappedFunctionVal
from thompson.nodes.literals import NoWrappingMappedFunctionVal
from thompson.nodes.ops import Assign, BindingRef, Funcall
from operator import add


def test_mapped_var(empty_context_eval):
    E = empty_context_eval
    E(Assign('x', MappedVal(42)))
    assert isinstance(E(BindingRef('x')), MappedVal)


def test_mapped_fun(empty_context_eval):
    E = empty_context_eval
    N = NumberVal
    E(Assign('add', MappedFunctionVal(add)))
    result = E(Funcall(BindingRef('add'), [N(1), N(2)]))
    assert result == N(3)


def simple_str_fun(s):
    return s * 3


def simple_bool_fun(b):
    return not b


def always_none(v):
    assert v is None
    return None


def test_mapped_fun_unwrap_and_wrap(empty_context_eval):
    E = empty_context_eval
    S, B = StringVal, BoolVal
    E(Assign('simple_str_fun', MappedFunctionVal(simple_str_fun)))
    E(Assign('simple_bool_fun', MappedFunctionVal(simple_bool_fun)))
    E(Assign('always_none', MappedFunctionVal(always_none)))
    # str.
    result = E(Funcall(BindingRef('simple_str_fun'), [S('foo')]))
    assert result == S('foofoofoo')
    # bool.
    result = E(Funcall(BindingRef('simple_bool_fun'), [B(True)]))
    assert result == B(False)
    # none.
    result = E(Funcall(BindingRef('always_none'), [NilConst]))
    assert result == NilConst


def dict_create():
    return {}


def dict_put(d, k, v):
    d[k] = v


def dict_get(d, k):
    return d[k]


def test_mapped_dict_funs(empty_context_eval):
    E = empty_context_eval
    S = StringVal
    E(Assign('dict_create', MappedFunctionVal(dict_create)))
    E(Assign('dict_put', MappedFunctionVal(dict_put)))
    E(Assign('dict_get', MappedFunctionVal(dict_get)))
    #
    d = E(Funcall(BindingRef('dict_create'), []))
    assert isinstance(d, MappedVal)
    E(Funcall(BindingRef('dict_put'), [d, S('foo'), S('bar')]))
    result = E(Funcall(BindingRef('dict_get'), [d, S('foo')]))
    assert result == S('bar')


def str_mult(s, times):
    S = StringVal
    s_ = s.get()
    times_ = times.get()
    return S(s_ * times_)


def test_no_wrapping_mapped_fun(empty_context_eval):
    E = empty_context_eval
    S, N = StringVal, NumberVal
    E(Assign('str_mult', NoWrappingMappedFunctionVal(str_mult)))
    #
    result = E(Funcall(BindingRef('str_mult'), [S('foo'), N(3)]))
    assert result == S('foo' * 3)
