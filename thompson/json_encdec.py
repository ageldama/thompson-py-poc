# -*- coding: utf-8 -*-
import json
from thompson.nodes import Node
from thompson.nodes.literals import BoolVal, StringVal, NumberVal
from thompson.nodes.literals import NullVal
from thompson.nodes.literals import FunctionVal
from thompson.nodes.literals import FunctionParamVal
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


class NodeJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.to_json_default(self)


def dumps(node: 'Node') -> str:
    return json.dumps(node, cls=NodeJsonEncoder)


__dict_to_objs__ = {
    'bool': BoolVal,
    'null': NullVal,
    'str': StringVal,
    'num': NumberVal,
    'fun-param': FunctionParamVal,
    'fun': [FunctionVal, 'params', 'body'],
    'prog1': Prog1,
    'progn': ProgN,
    'parprog': ParProg,
    'log-and': [LogAnd, 'a', 'b'],
    'log-or': [LogOr, 'a', 'b'],
    'log-not': LogNot,
    'add': [ArithAdd, 'a', 'b'],
    'sub': [ArithSub, 'a', 'b'],
    'mult': [ArithMult, 'a', 'b'],
    'multmult': [ArithMultMult, 'a', 'nth'],
    'div': [ArithDiv, 'numerator', 'denominator'],
    'divdiv': [ArithDivDiv, 'numerator', 'denominator'],
    'rem': [ArithRem, 'numerator', 'denominator'],
    'lt?': [ComparLt, 'a', 'b'],
    'le?': [ComparLe, 'a', 'b'],
    'gt?': [ComparGt, 'a', 'b'],
    'ge?': [ComparGe, 'a', 'b'],
    'eq?': [Equal, 'a', 'b'],
    'ne?': [NotEqual, 'a', 'b'],
    'null?': IsNull,
    'not-null?': IsNotNull,
    'assign': [Assign, 'dst', 'src'],
    'assign-upvar': [AssignUpvar, 'dst', 'src'],
    'assign-global': [AssignGlobal, 'dst', 'src'],
    'const': [Const, 'dst', 'src'],
    'let': [Let, 'exprs', 'body'],
    'ref': BindingRef,
    'pass': Pass,
    'funcall': [Funcall, 'fun', 'params'],
    'if': [IfThenElse, 'cond', 'then', 'else'],
    'when': [When, 'cond', 'then'],
    'unless': [Unless, 'cond', 'then'],
    'case-item': [CaseItem, 'v', 'then'],
    'case-else': [CaseElse, 'v', 'case-items', 'else'],
    'cond-item': [CondItem, 'cond', 'then'],
    'cond-else': [CondElse, 'cond-items', 'else'],
}


class DictToNodeTransformer(object):
    def __init__(self, *args, **kargs):
        pass

    def gather_params(self, d, ks):
        if isinstance(d, Node):
            return d
        else:
            return [self.dict_to_object(d[k]) for k in ks]

    def dict_to_object(self, d):
        keywords = __dict_to_objs__.keys()
        if isinstance(d, dict):
            k = set(d.keys()).pop()  # thus, it should has only 1-key.
            if k in keywords:
                ctor = __dict_to_objs__[k]
                if callable(ctor):
                    return ctor(self.dict_to_object(d[k]))
                else:
                    return ctor[0](*self.gather_params(d[k], ctor[1:]))
            else:
                return d
        elif isinstance(d, (tuple, list)):
            return [self.dict_to_object(i) for i in d]
        else:
            return d


def loads(s: str) -> 'Node':
    d = json.loads(s)
    transformer = DictToNodeTransformer()
    return transformer.dict_to_object(d)
