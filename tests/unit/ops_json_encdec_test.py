# -*- coding: utf-8 -*-
import json
from pytest import fixture
from thompson.nodes import Node
from thompson.nodes.ops.sequentials import Prog1, ProgN, ParProg
from thompson.nodes.ops.log_ops import LogAnd, LogOr, LogNot
from thompson.nodes.ops.arith_ops import ArithAdd, ArithSub
from thompson.nodes.ops.arith_ops import ArithMult, ArithMultMult
from thompson.nodes.ops.arith_ops import ArithDiv, ArithDivDiv
from thompson.nodes.ops.arith_ops import ArithRem
from thompson.nodes.ops.compar_ops import ComparLt, ComparLe
from thompson.nodes.ops.compar_ops import ComparGt, ComparGe
from thompson.nodes.ops.equals_and_nullity import Equal, NotEqual
from thompson.nodes.ops.equals_and_nullity import IsNull, IsNotNull  # noqa: E501
from thompson.nodes.ops.assigns import Assign, AssignUpvar, AssignGlobal  # noqa: E501
from thompson.nodes.ops.assigns import Const, BindingRef, Let
from thompson.nodes.ops.conditionals import IfThenElse, When, Unless  # noqa: E501
from thompson.nodes.ops.conditionals import CaseItem, CaseElse
from thompson.nodes.ops.conditionals import CondItem, CondElse
from thompson.nodes.ops.misc import Pass, Funcall
from thompson.json_encdec import NodeJsonEncoder
from thompson.json_encdec import NodeJsonDecoder
from thompson.nodes.literals import NumberVal, BoolVal


val_and_json_alist = [
    ('assign', (Assign('x', NumberVal(42)),
                """{"assign": {"dst": "x", "src": {"num": 42}}}""")),
    ('assign-upvar', (AssignUpvar('x', NumberVal(42)),
                      """{"assign-upvar": {"dst": "x", "src": {"num": 42}}}""")),  # noqa: E501
    ('assign-global', (AssignGlobal('x', NumberVal(42)),
                       """{"assign-global": {"dst": "x", "src": {"num": 42}}}""")),  # noqa: E501
    ('pass', (Pass(), '{"pass": 42}')),
    ('log-not', (LogNot(BindingRef('x')), '{"log-not": {"ref": "x"}}')),
    ('log-and', (LogAnd(BindingRef('x'), BoolVal(True)),
                 '{"log-and": {"a": {"ref": "x"}, "b": {"bool":true}}}')),
    ('log-or', (LogOr(BindingRef('x'), BoolVal(True)),
                '{"log-or": {"a": {"ref": "x"}, "b": {"bool":true}}}')),
    ('add', (ArithAdd(BindingRef('x'), BindingRef('y')),
             """{"add": {"a": {"ref": "x"},"b": {"ref": "y"}}}""")),
    ('sub', (ArithSub(BindingRef('x'), BindingRef('y')),
             """{"sub": {"a": {"ref": "x"},"b": {"ref": "y"}}}""")),
    ('mult', (ArithMult(BindingRef('x'), BindingRef('y')),
              """{"mult": {"a": {"ref": "x"},"b": {"ref": "y"}}}""")),
    ('multmult', (ArithMultMult(BindingRef('x'), BindingRef('y')),
                  """{"multmult": {"a": {"ref": "x"},
                  "nth": {"ref": "y"}}}""")),
    ('div', (ArithDiv(BindingRef('x'), BindingRef('y')),
             """{"div": {"numerator": {"ref": "x"},
             "denominator": {"ref": "y"}}}""")),
    ('divdiv', (ArithDivDiv(BindingRef('x'), BindingRef('y')),
                """{"divdiv": {"numerator": {"ref": "x"},
                "denominator": {"ref": "y"}}}""")),
    ('rem', (ArithRem(BindingRef('x'), BindingRef('y')),
             """{"rem": {"numerator": {"ref": "x"},
             "denominator": {"ref": "y"}}}""")),
    ('null?', (IsNull(BindingRef('x')), '{"null?": {"ref": "x"}}'),
     (IsNotNull(BindingRef('x')), '{"not-null?": {"ref": "x"}}')),
    ('const', (Const('pi', Funcall('rand', [])),
               """{"const": {"dst": "pi",
               "src": {"funcall": {"fun": "rand", "params": []}}}}""")),
    ('funcall0', (Funcall(BindingRef('rand'), []),
                  '{"funcall": {"fun": {"ref": "rand"}, "params": []}}')),
    ('lt', (ComparLt(BindingRef('x'), BindingRef('y')),
            """{"lt?": {"a": {"ref": "x"},"b": {"ref": "y"}}}""")),
    ('le', (ComparLe(BindingRef('x'), BindingRef('y')),
            """{"le?": {"a": {"ref": "x"},"b": {"ref": "y"}}}""")),
    ('gt', (ComparGt(BindingRef('x'), BindingRef('y')),
            """{"gt?": {"a": {"ref": "x"},"b": {"ref": "y"}}}""")),
    ('ge', (ComparGe(BindingRef('x'), BindingRef('y')),
            """{"ge?": {"a": {"ref": "x"},"b": {"ref": "y"}}}""")),
    ('eq?', (Equal(BindingRef('x'), BindingRef('y')),
             """{"eq?": {"a": {"ref": "x"},"b": {"ref": "y"}}}""")),
    ('ne?', (NotEqual(BindingRef('x'), BindingRef('y')),
             """{"ne?": {"a": {"ref": "x"},"b": {"ref": "y"}}}""")),
    ('ref', (BindingRef('x'), '{"ref": "x"}'),
     (Const('pi', NumberVal(3.14)),
      '{"const": {"dst": "pi", "src": {"num": 3.14}}}')),
    ('let+', (Let([Assign('x', BoolVal(True)),
                   Const('pi', NumberVal(3.14))], NumberVal(42)),
              """{"let": {"exprs": [
                         {"assign": {"dst": "x", "src": {"bool": true}}},
                         {"const": {"dst": "pi", "src": {"num": 3.14}}}],
                  "body": {"num": 42}}}""")),
    ('let0', (Let([], NumberVal(42)),
              """{"let": {"exprs": [], "body": {"num": 42}}}""")),
    ('funcall2', (Funcall(BindingRef('add'),
                          [BindingRef('x'), BindingRef('y')]),
                  """{"funcall": {"fun": {"ref": "add"},
                  "params": [{"ref": "x"}, {"ref": "y"}]}}""")),
    ('prog1-', (Prog1([]), """{"prog1": []}""")),
    ('prog1+', (Prog1([BindingRef('x'), BindingRef('y')]),
                """{"prog1": [{"ref": "x"}, {"ref": "y"}]}""")),
    ('progn-', (ProgN([]), """{"progn": []}""")),
    ('progn+', (ProgN([BindingRef('x'), BindingRef('y')]),
                """{"progn": [{"ref": "x"}, {"ref": "y"}]}""")),
    ('parprog-', (ParProg([]), """{"parprog": []}""")),
    ('parprog+', (ParProg([BindingRef('x'), BindingRef('y')]),
                  """{"parprog": [{"ref": "x"}, {"ref": "y"}]}""")),
    ('if-then', (IfThenElse(Equal(BindingRef('x'), NumberVal(42)),
                   Assign('result', BoolVal(True))),
              """{"if": {"cond": {"eq?": {"a": {"ref": "x"}, "b": {"num": 42}}},
                         "else": null,
                         "then": {"assign": {"dst": "result",
                                             "src": {"bool": true}}}}}""")),
    ('when', (When(Equal(BindingRef('x'), NumberVal(42)),
                   Assign('result', BoolVal(True))),
              """{"when": {"cond": {"eq?": {"a": {"ref": "x"}, "b": {"num": 42}}},
                           "then": {"assign": {"dst": "result",
                                               "src": {"bool": true}}}}}""")),
    ('unless', (Unless(Equal(BindingRef('x'), NumberVal(42)),
                       Assign('result', BoolVal(True))),
              """{"unless": {"cond": {"eq?": {"a": {"ref": "x"}, "b": {"num": 42}}},
                           "then": {"assign": {"dst": "result",
                                               "src": {"bool": true}}}}}""")),
    ('if-then-else', (IfThenElse(Equal(BindingRef('x'), NumberVal(42)),
                                 Assign('result', BoolVal(True)),
                                 Assign('result', BoolVal(False))),
              """{"if": {"cond": {"eq?": {"a": {"ref": "x"}, "b": {"num": 42}}},
                         "then": {"assign": {"dst": "result",
                                             "src": {"bool": true}}},
                         "else": {"assign": {"dst": "result",
                                             "src": {"bool": false}}}}}""")),
    ('cond-else', (CondElse([CondItem(IsNull(BindingRef('x')), NumberVal(42)),
                             CondItem(Equal(BindingRef('y'), NumberVal(7)),
                                      BoolVal(True))],
                            NumberVal(3.14)),
                   """{"cond-else": {"cond-items": [
                     {"cond-item": {"cond": {"null?": {"ref": "x"}},
                                    "then": {"num": 42}}},
                     {"cond-item": {"cond": {"eq?": {"a": {"ref": "y"},
                                                     "b": {"num": 7}}},
                                    "then": {"bool": true}}}
                   ], "else": {"num": 3.14}}}""")),
]

val_and_json_alist_ = [
    # FIXME:
    ('case-else', (CaseElse(BindingRef('x'),
                            [CaseItem(BoolVal(True), NumberVal(42)),
                             CaseItem(NumberVal(42), NumberVal(777))],
                            NumberVal(3.14)),
                   """{"case-else": {"v": {"ref": "x"}, "case-items": [
                     {"case-item": {"v": {"bool": true},
                                    "then": {"num": 42}}},
                     {"case-item": {"v": {"num": 42},
                                    "then": {"num": 777}}}
                   ], "else": {"num": 3.14}}}""")),
]


@fixture(params=[i[1] for i in val_and_json_alist],
         ids=[i[0] for i in val_and_json_alist])
def value_and_json(request):
    return request.param


def literally_decode_json(s):
    return json.loads(s)


def test_json_encode_ops_nodes(value_and_json):
    val, json_str = value_and_json
    j = json.dumps(val, cls=NodeJsonEncoder)
    assert isinstance(j, str)
    assert literally_decode_json(j) == literally_decode_json(json_str)


def test_json_decode_ops_nodes(value_and_json):
    val, json_str = value_and_json
    o = json.loads(json_str, cls=NodeJsonDecoder)
    assert isinstance(o, Node)
    # TODO: assert o == val
