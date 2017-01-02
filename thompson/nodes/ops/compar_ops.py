# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode
from thompson.jsons import enc_default


class ComparLt(ExprNode):
    def __init__(self, a: 'Evaluatable', b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "ComparLt[{}, {}]".format(str(self.a), str(self.b))

    def __eq__(self, other) -> bool:
        if not isinstance(other, ComparLt):
            return False
        else:
            return self.a == other.a \
                and self.b == other.b

    def to_json_default(self, json_encoder):
        return {'cmp-lt': {'a':
                           enc_default(self.a, json_encoder),
                           'b':
                           enc_default(self.b, json_encoder)}}


class ComparLe(ExprNode):
    def __init__(self, a: 'Evaluatable', b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "ComparLe[{}, {}]".format(str(self.a), str(self.b))

    def __eq__(self, other) -> bool:
        if not isinstance(other, ComparLe):
            return False
        else:
            return self.a == other.a \
                and self.b == other.b

    def to_json_default(self, json_encoder):
        return {'cmp-le': {'a':
                           enc_default(self.a, json_encoder),
                           'b':
                           enc_default(self.b, json_encoder)}}


class ComparGt(ExprNode):
    def __init__(self, a: 'Evaluatable', b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "ComparGt[{}, {}]".format(str(self.a), str(self.b))

    def __eq__(self, other) -> bool:
        if not isinstance(other, ComparGt):
            return False
        else:
            return self.a == other.a \
                and self.b == other.b

    def to_json_default(self, json_encoder):
        return {'cmp-gt': {'a':
                           enc_default(self.a, json_encoder),
                           'b':
                           enc_default(self.b, json_encoder)}}


class ComparGe(ExprNode):
    def __init__(self, a: 'Evaluatable', b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "ComparGe[{}, {}]".format(str(self.a), str(self.b))

    def __eq__(self, other) -> bool:
        if not isinstance(other, ComparGe):
            return False
        else:
            return self.a == other.a \
                and self.b == other.b

    def to_json_default(self, json_encoder):
        return {'cmp-ge': {'a':
                           enc_default(self.a, json_encoder),
                           'b':
                           enc_default(self.b, json_encoder)}}
