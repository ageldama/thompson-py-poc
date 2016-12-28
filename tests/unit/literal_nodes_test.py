# -*- coding: utf-8; -*-
from pytest import raises, fixture
from thompson.literals import StringVal, NumberVal, BoolVal


def test_literal_nodes_type_oks():
    StringVal('')
    NumberVal(42)
    NumberVal(3.14)
    BoolVal(True)
    BoolVal(False)


@fixture(params=[(BoolVal, 42,), (BoolVal, '',),
                 (NumberVal, '42',), (NumberVal, True,),
                 (StringVal, 42,), (StringVal, 3.14,), (StringVal, True,)])
def literal_node_ctr_and_param(request):
    return request.param


def test_literal_nodes_type_fails(literal_node_ctr_and_param):
    (ctr, param,) = literal_node_ctr_and_param
    with raises(AssertionError):
        ctr(param)
