# -*- coding: utf-8; -*-
from pytest import raises, fixture
from thompson.nodes.literals import StringVal, NumberVal, BoolVal
from thompson.nodes.literals import NullVal, NilConst


def test_literal_nodes_type_oks():
    StringVal('')
    NumberVal(42)
    NumberVal(3.14)
    BoolVal(True)
    BoolVal(False)


@fixture(params=[(BoolVal, 42,), (BoolVal, '',),
                 (NumberVal, '42',), (NumberVal, True,),
                 (StringVal, 42,), (StringVal, 3.14,), (StringVal, True,)],
         ids=['BoolVal-with-int', 'BoolVal-with-str',
              'NumberVal-with-str', 'NumberVal-with-bool',
              'StringVal-with-int', 'StringVal-with-float',
              'StringVal-with-bool'])
def literal_node_ctr_and_param(request):
    return request.param


def test_literal_nodes_type_fails(literal_node_ctr_and_param):
    (ctr, param,) = literal_node_ctr_and_param
    with raises(AssertionError):
        ctr(param)


def test_literal_nodes_eqs():
    assert NullVal() == NullVal()
    assert NullVal() == NilConst
    assert StringVal('foobar') == StringVal("foo" + 'bar')
    assert StringVal('foobar') != StringVal('spameggs')
    assert BoolVal(True) == BoolVal(True)
    assert BoolVal(False) != BoolVal(True)
    assert NumberVal(42) == NumberVal(40 + 2)
    assert NumberVal(3.14) == NumberVal(3 + 0.14)
    assert NumberVal(42) == NumberVal(42.0)
