# -*- coding: utf-8; -*-
from thompson.nodes.literals import NilConst, NullVal, BoolVal
from thompson.nodes.literals import NumberVal, StringVal
from thompson.nodes.ops import Equal, NotEqual
from thompson.nodes.ops import IsNotNull, IsNull


def test_equality(empty_context_eval):
    E = empty_context_eval
    B, S, N = BoolVal, StringVal, NumberVal
    # eq.
    assert E(Equal(N(42), N(42.0))) == B(True)
    assert E(Equal(N(42), N(3.14))) == B(False)
    assert E(Equal(B(True), B(True))) == B(True)
    assert E(Equal(B(False), B(True))) == B(False)
    assert B(False) == E(Equal(N(42), N(-42)))
    assert B(True) == E(Equal(S('foo'), S('foo')))
    assert B(False) == E(Equal(S('bar'), S('foo')))
    assert B(True) == E(Equal(NullVal(), NilConst))
    assert B(False) == E(Equal(N(42), B(True)))
    assert B(False) == E(Equal(N(42), S('')))
    # ne.
    assert E(NotEqual(N(42), N(42.0))) == B(False)
    assert E(NotEqual(N(42), N(-42))) == B(True)
    assert E(NotEqual(S('foo'), S('bar'))) == B(True)
    assert E(NotEqual(S('foo'), N(42))) == B(True)


def test_nullity(empty_context_eval):
    E = empty_context_eval
    B, S, N = BoolVal, StringVal, NumberVal
    # null?
    assert B(True) == E(IsNull(NilConst))
    assert B(True) == E(IsNull(NullVal()))
    assert B(False) == E(IsNull(B(True)))
    # not-null?
    assert B(False) == E(IsNotNull(NilConst))
    assert B(False) == E(IsNotNull(NullVal()))
    assert B(True) == E(IsNotNull(B(True)))
    assert B(True) == E(IsNotNull(N(42)))
    assert B(True) == E(IsNotNull(S('')))
