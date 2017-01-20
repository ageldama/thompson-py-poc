# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode
from thompson.strs import to_joined_strs
from thompson.jsons import enc_defaults, enc_default
from thompson.eqs import eq_params


class LogAnd(ExprNode):
    def __init__(self, params: ['Evaluatable']) -> None:
        self.params = params

    def __str__(self) -> str:
        return "LogAnd[{}]".format(to_joined_strs(self.params))

    def __eq__(self, other) -> bool:
        return eq_params(self, other, LogAnd)

    def to_json_default(self, json_encoder):
        return {'log-and': enc_defaults(self.params, json_encoder)}


class LogOr(ExprNode):
    def __init__(self, params: ['Evaluatable']) -> None:
        self.params = params

    def __str__(self) -> str:
        return "LogOr[{}]".format(to_joined_strs(self.params))

    def __eq__(self, other) -> bool:
        return eq_params(self, other, LogOr)

    def to_json_default(self, json_encoder):
        return {'log-or': enc_defaults(self.params, json_encoder)}


class LogNot(ExprNode):
    def __init__(self, a: 'Evaluatable') -> None:
        self.a = a

    def __str__(self) -> str:
        return "LogNot[{}]".format(str(self.a))

    def __eq__(self, other) -> bool:
        if not isinstance(other, LogNot):
            return False
        else:
            return self.a == other.a

    def to_json_default(self, json_encoder):
        return {'log-not': enc_default(self.a, json_encoder)}
