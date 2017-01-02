# -*- coding: utf-8 -*-
import json
from pytest import fixture, raises
import math
from thompson.nodes.literals import BoolVal, StringVal, NumberVal
from thompson.nodes.literals import NilConst
from thompson.nodes.literals import FunctionParamVal
from thompson.nodes.literals import MappedVal, MappedFunctionVal
from thompson.nodes.literals import NoWrappingMappedFunctionVal
from thompson.json import LiteralNodeJsonEncoder
from thompson.json import LiteralNodeJsonDecoder


@fixture(params=[(BoolVal(True), '{"bool": true}'),
                 (NilConst, '{"null": null}'),
                 (NumberVal(42), '{"num": 42}'),
                 (NumberVal(-42), '{"num": -42}'),
                 (NumberVal(3.14), '{"num": 3.14}'),
                 (NumberVal(math.nan), '{"num": NaN}'),
                 (FunctionParamVal("a"), '{"fun-param": "a"}'),
                 (StringVal('foo'), '{"str": "foo"}')],
         ids=('bool-true', 'nil', 'num+42', 'num-42', 'num+3.14',
              'num-nan', 'func-param-val', 'str-foo'))
def value_and_json(request):
    return request.param


@fixture(params=(MappedVal('v'),
                 MappedFunctionVal('f', []),
                 NoWrappingMappedFunctionVal('f', [])),
         ids=('mapped-val',
              'mapped-fun-val',
              'no-wrapping-mapped-fun-val'))
def serialization_not_allowed_values(request):
    return request.param


def test_json_encode_LiteralNodes(value_and_json):
    val, json_str = value_and_json
    j = json.dumps(val, cls=LiteralNodeJsonEncoder)
    assert isinstance(j, str)
    assert json_str == j


def test_json_encode_not_alloweds(serialization_not_allowed_values):
    val = serialization_not_allowed_values
    with raises(ValueError):
        json.dumps(val, cls=LiteralNodeJsonEncoder)


def test_json_decode_LiteralNodes(value_and_json):
    val, json_str = value_and_json
    o = json.loads(json_str, cls=LiteralNodeJsonDecoder)
    assert isinstance(val, type(o))
    assert val == o
