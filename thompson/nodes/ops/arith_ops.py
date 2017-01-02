# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode


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
