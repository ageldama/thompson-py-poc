# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode
from thompson.jsons import enc_default


class LogAnd(ExprNode):
    def __init__(self,
                 a: 'Evaluatable',
                 b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "LogAnd[{}, {}]".format(str(self.a), str(self.b))

    def __eq__(self, other) -> bool:
        if not isinstance(other, LogAnd):
            return False
        else:
            return self.a == other.a and self.b == self.b

    def to_json_default(self, json_encoder):
        return {'log-and': {'a': enc_default(self.a, json_encoder),
                            'b': enc_default(self.b, json_encoder)}}


class LogOr(ExprNode):
    def __init__(self,
                 a: 'Evaluatable',
                 b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "LogOr[{}, {}]".format(str(self.a), str(self.b))

    def __eq__(self, other) -> bool:
        if not isinstance(other, LogOr):
            return False
        else:
            return self.a == other.a and self.b == self.b

    def to_json_default(self, json_encoder):
        return {'log-or': {'a': enc_default(self.a, json_encoder),
                           'b': enc_default(self.b, json_encoder)}}


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
