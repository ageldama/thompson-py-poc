# -*- coding: utf-8 -*-
import json
from thompson.nodes.literals import BoolVal, StringVal, NumberVal
from thompson.nodes.literals import NullVal
from thompson.nodes.literals import FunctionParamVal


class NodeJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.to_json_default(self)


class NodeJsonDecoder(json.JSONDecoder):
    def __init__(self, *args, **kargs):
        json.JSONDecoder.__init__(self, object_hook=self.dict_to_object,
                                  *args, **kargs)

    def dict_to_object(self, d):
        allowed_keys = {'num', 'str', 'bool', 'null', 'fun-param'}
        if isinstance(d, dict) and \
           0 < len(allowed_keys.intersection(d.keys())):
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
            return d


"""
** TODO prog1
** TODO progn
** TODO parprog
** TODO log-and
** TODO log-or
** TODO log-not
** TODO arith+
** TODO arith-
** TODO arith/
** TODO arith//
** TODO arith*
** TODO arith**
** TODO arith-rem
** TODO cmp-<
** TODO cmp-<=
** TODO cmp->
** TODO cmp->=
** TODO eq
** TODO ne
** TODO is-null
** TODO is-not-null
** TODO assign
** TODO assign-upvar
** TODO assign-global
** TODO const
** TODO binding-ref
** TODO let
** TODO if-then-else
** TODO when
** TODO unless
** TODO case-item
** TODO case-else
** TODO cond-item
** TODO cond-else
** TODO pass
** TODO funcall
"""
