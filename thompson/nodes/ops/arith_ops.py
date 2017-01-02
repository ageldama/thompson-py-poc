# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode


class ArithAdd(ExprNode):
    def __init__(self, a: 'Evaluatable', b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "ArithAdd[{}, {}]".format(str(self.a), str(self.b))


class ArithSub(ExprNode):
    def __init__(self, a: 'Evaluatable', b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "ArithSub[{}, {}]".format(str(self.a), str(self.b))


class ArithMult(ExprNode):
    def __init__(self, a: 'Evaluatable', b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "ArithMult[{}, {}]".format(str(self.a), str(self.b))


class ArithMultMult(ExprNode):
    def __init__(self, a: 'Evaluatable', nth: 'Evaluatable') -> None:
        self.a, self.nth = a, nth

    def __str__(self) -> str:
        return "ArithMultMult[{}, nth={}]".format(str(self.a), str(self.nth))


class ArithDiv(ExprNode):
    def __init__(self, numerator: 'Evaluatable',
                 denominator: 'Evaluatable') -> None:
        self.numerator, self.denominator = numerator, denominator

    def __str__(self) -> str:
        return "ArithDiv[numerator={}, denominator={}]".format(
            str(self.numerator, str(self.denominator)))


class ArithRem(ExprNode):
    def __init__(self, numerator: 'Evaluatable',
                 denominator: 'Evaluatable') -> None:
        self.numerator, self.denominator = numerator, denominator

    def __str__(self) -> str:
        return "ArithRem[numerator={}, denominator={}]".format(
            str(self.numerator, str(self.denominator)))


class ArithDivDiv(ExprNode):
    def __init__(self, numerator: 'Evaluatable',
                 denominator: 'Evaluatable') -> None:
        self.numerator, self.denominator = numerator, denominator

    def __str__(self) -> str:
        return "ArithDivDiv[numerator={}, denominator={}]".format(
            str(self.numerator, str(self.denominator)))
