# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode
from thompson.jsons import enc_default


class Equal(ExprNode):
    def __init__(self,
                 a: 'Evaluatable',
                 b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "Equal[{}, {}]".format(str(self.a), str(self.b))

    def __eq__(self, other) -> bool:
        if not isinstance(other, Equal):
            return False
        else:
            return self.a == other.a \
                and self.b == other.b

    def to_json_default(self, json_encoder):
        return {'eq?': {'a': enc_default(self.a, json_encoder),
                        'b': enc_default(self.b, json_encoder)}}


class NotEqual(ExprNode):
    def __init__(self,
                 a: 'Evaluatable',
                 b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "NotEqual[{}, {}]".format(str(self.a), str(self.b))

    def __eq__(self, other) -> bool:
        if not isinstance(other, NotEqual):
            return False
        else:
            return self.a == other.a \
                and self.b == other.b

    def to_json_default(self, json_encoder):
        return {'ne?': {'a': enc_default(self.a, json_encoder),
                        'b': enc_default(self.b, json_encoder)}}


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
