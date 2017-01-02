# coding: utf-8
from pytest import fixture
from thompson.nodes.literals import BoolVal, NullVal, NilConst
from thompson.nodes.literals import StringVal, NumberVal
# from thompson.nodes.literals import FunctionVal
from thompson.nodes.literals import FunctionParamVal
from thompson.nodes.literals import MappedVal, MappedFunctionVal
from thompson.nodes.literals import NoWrappingMappedFunctionVal
from math import nan, inf


# TODO: fun-val

@fixture(params=((StringVal('a'), StringVal('A'.lower())),
                 (NullVal(), NilConst),
                 (BoolVal(True), BoolVal(True)),
                 (BoolVal(False), BoolVal(False)),
                 (NumberVal(42.1), NumberVal(42.1)),
                 (NumberVal(nan), NumberVal(nan)),
                 (NumberVal(-nan), NumberVal(nan)),
                 (NumberVal(inf), NumberVal(inf)),
                 (NumberVal(-inf), NumberVal(inf)),
                 (MappedVal('a'), MappedVal('a')),
                 (MappedFunctionVal('a', [FunctionParamVal('p')]),
                  MappedFunctionVal('a', [FunctionParamVal('p')])),
                 (NoWrappingMappedFunctionVal('a', [FunctionParamVal('p')]),
                  NoWrappingMappedFunctionVal('a', [FunctionParamVal('p')])),
                 (FunctionParamVal('a'), FunctionParamVal('a'))),
         ids=('str',
              'nulls',
              'bool-t',
              'bool-f',
              'num+42',
              'num+nan',
              'num+-nan',
              'num+inf',
              'num-+inf',
              'mapped-val',
              'mapped-fun-val+fun-vals',
              'no-wrapping-mapped-fun-val+fun-vals',
              'fun-param-val'))
def a_and_b(request):
    return request.param


def test_eq(a_and_b):
    a, b = a_and_b
    assert a == b
