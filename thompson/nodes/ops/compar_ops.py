# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode
from thompson.strs import to_joined_strs
from thompson.jsons import enc_defaults
from thompson.eqs import eq_params


class ComparLt(ExprNode):
    def __init__(self, params: ['Evaluatable']) -> None:
        self.params = params

    def __str__(self) -> str:
        return "ComparLt[{}]".format(to_joined_strs(self.params))

    def __eq__(self, other) -> bool:
        return eq_params(self, other, ComparLt)

    def to_json_default(self, json_encoder):
        return {'lt?': enc_defaults(self.params, json_encoder)}


class ComparLe(ExprNode):
    def __init__(self, params: ['Evaluatable']) -> None:
        self.params = params

    def __str__(self) -> str:
        return "ComparLe[{}]".format(to_joined_strs(self.params))

    def __eq__(self, other) -> bool:
        return eq_params(self, other, ComparLe)

    def to_json_default(self, json_encoder):
        return {'le?': enc_defaults(self.params, json_encoder)}


class ComparGt(ExprNode):
    def __init__(self, params: ['Evaluatable']) -> None:
        self.params = params

    def __str__(self) -> str:
        return "ComparGt[{}]".format(to_joined_strs(self.params))

    def __eq__(self, other) -> bool:
        return eq_params(self, other, ComparGt)

    def to_json_default(self, json_encoder):
        return {'gt?': enc_defaults(self.params, json_encoder)}


class ComparGe(ExprNode):
    def __init__(self, params: ['Evaluatable']) -> None:
        self.params = params

    def __str__(self) -> str:
        return "ComparGe[{}]".format(to_joined_strs(self.params))

    def __eq__(self, other) -> bool:
        return eq_params(self, other, ComparGe)

    def to_json_default(self, json_encoder):
        return {'ge?': enc_defaults(self.params, json_encoder)}
