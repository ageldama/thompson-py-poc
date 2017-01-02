# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode
from thompson.jsons import enc_default


class ArithAdd(ExprNode):
    def __init__(self, a: 'Evaluatable', b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "ArithAdd[{}, {}]".format(str(self.a), str(self.b))

    def __eq__(self, other) -> bool:
        if not isinstance(other, ArithAdd):
            return False
        else:
            return self.a == self.a and self.b == self.b

    def to_json_default(self, json_encoder):
        return {'add': {'a': enc_default(self.a, json_encoder),
                        'b': enc_default(self.b, json_encoder)}}


class ArithSub(ExprNode):
    def __init__(self, a: 'Evaluatable', b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "ArithSub[{}, {}]".format(str(self.a), str(self.b))

    def __eq__(self, other) -> bool:
        if not isinstance(other, ArithSub):
            return False
        else:
            return self.a == self.a and self.b == self.b

    def to_json_default(self, json_encoder):
        return {'sub': {'a': enc_default(self.a, json_encoder),
                        'b': enc_default(self.b, json_encoder)}}


class ArithMult(ExprNode):
    def __init__(self, a: 'Evaluatable', b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "ArithMult[{}, {}]".format(str(self.a), str(self.b))

    def __eq__(self, other) -> bool:
        if not isinstance(other, ArithMult):
            return False
        else:
            return self.a == self.a and self.b == self.b

    def to_json_default(self, json_encoder):
        return {'mult': {'a': enc_default(self.a, json_encoder),
                         'b': enc_default(self.b, json_encoder)}}


class ArithMultMult(ExprNode):
    def __init__(self, a: 'Evaluatable', nth: 'Evaluatable') -> None:
        self.a, self.nth = a, nth

    def __str__(self) -> str:
        return "ArithMultMult[{}, nth={}]".format(str(self.a), str(self.nth))

    def __eq__(self, other) -> bool:
        if not isinstance(other, ArithMultMult):
            return False
        else:
            return self.a == self.a and self.nth == self.nth

    def to_json_default(self, json_encoder):
        return {'multmult': {'a': enc_default(self.a, json_encoder),
                             'nth': enc_default(self.nth, json_encoder)}}


class ArithDiv(ExprNode):
    def __init__(self, numerator: 'Evaluatable',
                 denominator: 'Evaluatable') -> None:
        self.numerator, self.denominator = numerator, denominator

    def __str__(self) -> str:
        return "ArithDiv[numerator={}, denominator={}]".format(
            str(self.numerator, str(self.denominator)))

    def __eq__(self, other) -> bool:
        if not isinstance(other, ArithDiv):
            return False
        else:
            return self.numerator == self.numerator \
                and self.denominator == self.denominator

    def to_json_default(self, json_encoder):
        return {'div': {'numerator':
                        enc_default(self.numerator, json_encoder),
                        'denominator':
                        enc_default(self.denominator, json_encoder)}}


class ArithRem(ExprNode):
    def __init__(self, numerator: 'Evaluatable',
                 denominator: 'Evaluatable') -> None:
        self.numerator, self.denominator = numerator, denominator

    def __str__(self) -> str:
        return "ArithRem[numerator={}, denominator={}]".format(
            str(self.numerator, str(self.denominator)))

    def __eq__(self, other) -> bool:
        if not isinstance(other, ArithRem):
            return False
        else:
            return self.numerator == self.numerator \
                and self.denominator == self.denominator

    def to_json_default(self, json_encoder):
        return {'rem': {'numerator':
                        enc_default(self.numerator, json_encoder),
                        'denominator':
                        enc_default(self.denominator, json_encoder)}}


class ArithDivDiv(ExprNode):
    def __init__(self, numerator: 'Evaluatable',
                 denominator: 'Evaluatable') -> None:
        self.numerator, self.denominator = numerator, denominator

    def __str__(self) -> str:
        return "ArithDivDiv[numerator={}, denominator={}]".format(
            str(self.numerator, str(self.denominator)))

    def __eq__(self, other) -> bool:
        if not isinstance(other, ArithDivDiv):
            return False
        else:
            return self.numerator == self.numerator \
                and self.denominator == self.denominator

    def to_json_default(self, json_encoder):
        return {'divdiv': {'numerator':
                           enc_default(self.numerator, json_encoder),
                           'denominator':
                           enc_default(self.denominator, json_encoder)}}
