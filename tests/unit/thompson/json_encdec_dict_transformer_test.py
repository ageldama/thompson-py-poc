# -*- coding: utf-8; -*-
from pytest import fixture
from thompson.json_encdec import DictToNodeTransformer
from thompson.nodes.literals import NumberVal, BoolVal, StringVal
from thompson.nodes.ops import IsNull, Equal
from thompson.nodes.ops import CondElse, CondItem
from thompson.nodes.ops import Pass, Funcall
from thompson.nodes.ops import BindingRef
from thompson.nodes.ops import ProgN, Prog1
from thompson.nodes import Node


__dict_and_nodes = [
    ('num+42', ({"num": 42}, NumberVal(42))),
    ('bool-true', ({"bool": True}, BoolVal(True))),
    ('binding-ref', ({"ref": "x"}, BindingRef('x'))),
    ('pass', ({"pass": 42}, Pass())),
    ('progn-0', ({"progn": []}, ProgN([]))),
    ('prog1-0', ({"prog1": []}, Prog1([]))),
    ('funcall-0', ({'funcall': {'fun': {'ref': 'f'}, 'params': []}},
                   Funcall(BindingRef('f'), []))),
    ('binding-ref-with-str-val',
     ({"ref": {"str": "x"}},
      BindingRef(StringVal('x')))),
    ('prog1+', ({"prog1": [{"ref": "x"}, {"ref": "y"}]},
                Prog1([BindingRef('x'), BindingRef('y')]))),
    ('cond-else', ({"cond-else": {"cond-items": [
        {"cond-item": {"cond": {"null?": {"ref": "x"}},
                       "then": {"num": 42}}},
        {"cond-item": {"cond": {"eq?": [{"ref": "y"}, {"num": 7}]},
                       "then": {"bool": True}}}],
                                  "else": {"num": 3.14}}},
                   CondElse([CondItem(IsNull(BindingRef('x')), NumberVal(42)),
                             CondItem(Equal([BindingRef('y'), NumberVal(7)]),
                                      BoolVal(True))],
                            NumberVal(3.14)))),
]


@fixture(params=[i[1] for i in __dict_and_nodes],
         ids=[i[0] for i in __dict_and_nodes])
def dict_and_nodes(request):
    return request.param


def test_transform(dict_and_nodes):
    d, node = dict_and_nodes
    transformer = DictToNodeTransformer()
    node2 = transformer.dict_to_object(d)
    assert isinstance(node2, Node)
    try:
        assert node2 == node
    except Exception as exc:
        raise exc
