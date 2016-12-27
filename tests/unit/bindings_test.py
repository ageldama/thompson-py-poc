# -*- coding: utf-8; -*-

from pytest import raises
from thompson.bindings import Binding


def test_creation():
    b_wo_parent = Binding()
    assert b_wo_parent.parent is None
    #
    b_with_parent = Binding(b_wo_parent)
    assert b_with_parent is not None


def test_simplest_set_and_get_without_inherits():
    b = Binding()
    k = "the-answer"
    v = 42
    #
    with raises(NameError):
        b.get_no_inherits(k)
    #
    b.set(k, v)
    assert v == b.get_no_inherits(k)


def test_contains_without_inherits():
    b = Binding()
    k = "the-answer"
    another_k = "the-wrong-answer"
    v = 42
    #
    b.set(k, v)
    assert b.contains_no_inherits(k)
    assert not b.contains_no_inherits(another_k)


def test_set_uplevel_and_get_also_contains():
    b_grandparent = Binding()
    b_parent = Binding(b_grandparent)
    b = Binding(b_parent)
    k = "the-answer"
    v = 42
    #
    with raises(ValueError):
        b_grandparent.set_uplevel(k, v)
    #
    b_parent.set_uplevel(k, v)
    assert b.parent.contains(k)
    assert not b.parent.contains_no_inherits(k)
    assert b.parent.parent.contains_no_inherits(k)
    assert not b.contains_no_inherits(k)
    assert b.contains(k)
    with raises(NameError):
        b.get_no_inherits(k)
    assert v == b.get(k)
    assert v == b.parent.get(k)
    assert v == b.parent.parent.get(k)
    assert v == b.parent.parent.get_no_inherits(k)


def test_set_global():
    b_grandparent = Binding()
    b_parent = Binding(b_grandparent)
    b = Binding(b_parent)
    k = "the-answer"
    v = 42
    #
    b.set_global(k, v)
    assert b.get(k) == v
    assert not b.contains_no_inherits(k)
    assert b.parent.get(k) == v
    assert not b.parent.contains_no_inherits(k)
    assert b.parent.parent.get(k) == v
