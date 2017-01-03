# -*- coding: utf-8 -*-
import json
from typing import Sequence, Callable
from thompson.nodes.literals import BoolVal, StringVal, NumberVal
from thompson.nodes.literals import NullVal
from thompson.nodes.literals import FunctionParamVal
from thompson.nodes.ops.sequentials import Prog1, ProgN, ParProg  # noqa: F401
from thompson.nodes.ops.log_ops import LogAnd, LogOr, LogNot  # noqa: F401
from thompson.nodes.ops.arith_ops import ArithAdd, ArithSub  # noqa: F401
from thompson.nodes.ops.arith_ops import ArithMult, ArithMultMult  # noqa: F401
from thompson.nodes.ops.arith_ops import ArithDiv, ArithDivDiv  # noqa: F401
from thompson.nodes.ops.arith_ops import ArithRem  # noqa: F401
from thompson.nodes.ops.compar_ops import ComparLt, ComparLe  # noqa: F401
from thompson.nodes.ops.compar_ops import ComparGt, ComparGe  # noqa: F401
from thompson.nodes.ops.equals_and_nullity import Equal, NotEqual  # noqa: F401
from thompson.nodes.ops.equals_and_nullity import IsNull, IsNotNull  # noqa: F401, E501
from thompson.nodes.ops.assigns import Assign, AssignUpvar, AssignGlobal  # noqa: F401, E501
from thompson.nodes.ops.assigns import Const, BindingRef, Let  # noqa: F401
from thompson.nodes.ops.conditionals import IfThenElse, When, Unless  # noqa: F401, E501
from thompson.nodes.ops.conditionals import CaseItem, CaseElse  # noqa: F401
from thompson.nodes.ops.conditionals import CondItem, CondElse  # noqa: F401
from thompson.nodes.ops.misc import Pass, Funcall  # noqa: F401


class NodeJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.to_json_default(self)


__dict_to_objs__ = {
    'progn1': Prog1,
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
    'case': [CaseElse, 'v', 'case-items', 'else'],
    'cond-item': [CondItem, 'cond', 'then'],
    'cond': [CondElse, 'cond-items', 'else'],
}


class NodeJsonDecoder(json.JSONDecoder):
    def __init__(self, *args, **kargs):
        json.JSONDecoder.__init__(self, object_hook=self.dict_to_object,
                                  *args, **kargs)

    def dict_to_object(self, d):
        allowed_keys = {'num', 'str', 'bool', 'null', 'fun-param'}
        if isinstance(d, dict):
            if 0 < len(allowed_keys.intersection(d.keys())):
                ks = d.keys()
                vs = d.values()
                k_and_ctor = (('bool', BoolVal),
                              ('str', StringVal),
                              ('num', NumberVal),
                              ('null', NullVal),
                              ('fun-param', FunctionParamVal))
                for k, ctor in k_and_ctor:
                    if k in ks:
                        return ctor(*vs)
                raise KeyError("Cannot be instantiated {} type".format(ks))
            else:
                ks = d.keys()
                if len(ks) == 1:
                    k = set(ks).pop()
                    if k in __dict_to_objs__.keys():
                        to_obj = __dict_to_objs__[k]
                        assert to_obj is not None
                        if isinstance(to_obj, Sequence):
                            to_obj_ = to_obj[0]
                            assert isinstance(to_obj_, Callable)
                            assert isinstance(to_obj[1:], Sequence)
                            assert to_obj[1:] is not None
                            print(d, k)
                            return to_obj_(*self.__by_keys(d[k], to_obj[1:]))
                        else:
                            return to_obj(self.dict_to_object(d[k]))
                    else:
                        raise KeyError(
                            "Unsupported JSON node for '{}'".format(k))
        else:
            return d

    def __by_keys(self, d, ks):
        print(d, ks)
        return [self.dict_to_object(d[k]) for k in ks]
