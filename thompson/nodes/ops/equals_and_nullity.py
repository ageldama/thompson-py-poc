# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode
from thompson.strs import to_joined_strs
from thompson.jsons import enc_defaults, enc_default
from thompson.eqs import eq_params


class Equal(ExprNode):
    def __init__(self, params: ['Evaluatable']) -> None:
        self.params = params

    def __str__(self) -> str:
        return "Equal[{}]".format(to_joined_strs(self.params))

    def __eq__(self, other) -> bool:
        return eq_params(self, other, Equal)

    def to_json_default(self, json_encoder):
        return {'eq?': enc_defaults(self.params, json_encoder)}


class NotEqual(ExprNode):
    def __init__(self, params: ['Evaluatable']) -> None:
        self.params = params

    def __str__(self) -> str:
        return "NotEqual[{}]".format(to_joined_strs(self.params))

    def __eq__(self, other) -> bool:
        return eq_params(self, other, NotEqual)

    def to_json_default(self, json_encoder):
        return {'ne?': enc_defaults(self.params, json_encoder)}


class IsNull(ExprNode):
    def __init__(self, a: 'Evaluatable') -> None:
        self.a = a

    def __str__(self) -> str:
        return "IsNull[{}]".format(str(self.a))

    def __eq__(self, other) -> bool:
        if not isinstance(other, IsNull):
            return False
        else:
            return self.a == other.a

    def to_json_default(self, json_encoder):
        return {'null?': enc_default(self.a, json_encoder)}


class IsNotNull(ExprNode):
    def __init__(self, a: 'Evaluatable') -> None:
        self.a = a

    def __str__(self) -> str:
        return "IsNotNull[{}]".format(str(self.a))

    def __eq__(self, other) -> bool:
        if not isinstance(other, IsNotNull):
            return False
        else:
            return self.a == other.a

    def to_json_default(self, json_encoder):
        return {'not-null?': enc_default(self.a, json_encoder)}
