# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode
from thompson.strs import to_joined_strs
from thompson.jsons import enc_defaults, enc_default
from thompson.eqs import eq_params


class ArithAdd(ExprNode):
    def __init__(self, params: ['Evaluatable']) -> None:
        self.params = params

    def __str__(self) -> str:
        return "ArithAdd[{}]".format(to_joined_strs(self.params))

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        return eq_params(self, other, ArithAdd)

    def to_json_default(self, json_encoder):
        return {'add': enc_defaults(self.params, json_encoder)}


class ArithSub(ExprNode):
    def __init__(self, params: ['Evaluatable']) -> None:
        self.params = params

    def __str__(self) -> str:
        return "ArithSub[{}]".format(to_joined_strs(self.params))

    def __eq__(self, other) -> bool:
        return eq_params(self, other, ArithSub)

    def to_json_default(self, json_encoder):
        return {'sub': enc_defaults(self.params, json_encoder)}


class ArithMult(ExprNode):
    def __init__(self, params: ['Evaluatable']) -> None:
        self.params = params

    def __str__(self) -> str:
        return "ArithMult[{}]".format(to_joined_strs(self.params))

    def __eq__(self, other) -> bool:
        return eq_params(self, other, ArithMult)

    def to_json_default(self, json_encoder):
        return {'mult': enc_defaults(self.params, json_encoder)}


class ArithMultMult(ExprNode):
    def __init__(self, params: ['Evaluatable']) -> None:
        self.params = params

    def __str__(self) -> str:
        return "ArithMultMult[{}]".format(to_joined_strs(self.params))

    def __eq__(self, other) -> bool:
        return eq_params(self, other, ArithMultMult)

    def to_json_default(self, json_encoder):
        return {'multmult': enc_defaults(self.params, json_encoder)}


class ArithDiv(ExprNode):
    def __init__(self, params: ['Evaluatable']) -> None:
        self.params = params

    def __str__(self) -> str:
        return "ArithDiv[{}]".format(to_joined_strs(self.params))

    def __eq__(self, other) -> bool:
        return eq_params(self, other, ArithDiv)

    def to_json_default(self, json_encoder):
        return {'div': enc_defaults(self.params, json_encoder)}


class ArithRem(ExprNode):
    def __init__(self, params: ['Evaluatable']) -> None:
        self.params = params

    def __str__(self) -> str:
        return "ArithRem[{}]".format(to_joined_strs(self.params))

    def __eq__(self, other) -> bool:
        return eq_params(self, other, ArithRem)

    def to_json_default(self, json_encoder):
        return {'rem': enc_defaults(self.params, json_encoder)}


class ArithDivDiv(ExprNode):
    def __init__(self, params: ['Evaluatable']) -> None:
        self.params = params

    def __str__(self) -> str:
        return "ArithDivDiv[{}]".format(to_joined_strs(self.params))

    def __eq__(self, other) -> bool:
        return eq_params(self, other, ArithDivDiv)

    def to_json_default(self, json_encoder):
        return {'divdiv': enc_defaults(self.params, json_encoder)}
