# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode


class ArithAdd(ExprNode):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __str__(self):
        return "ArithAdd[{}, {}]".format(str(self.a), str(self.b))


class ArithSub(ExprNode):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __str__(self):
        return "ArithSub[{}, {}]".format(str(self.a), str(self.b))


class ArithMult(ExprNode):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __str__(self):
        return "ArithMult[{}, {}]".format(str(self.a), str(self.b))


class ArithMultMult(ExprNode):
    def __init__(self, a, nth):
        self.a, self.nth = a, nth

    def __str__(self):
        return "ArithMultMult[{}, nth={}]".format(str(self.a), str(self.nth))


class ArithDiv(ExprNode):
    def __init__(self, numerator, denominator):
        self.numerator, self.denominator = numerator, denominator

    def __str__(self):
        return "ArithDiv[numerator={}, denominator={}]".format(
            str(self.numerator, str(self.denominator)))


class ArithRem(ExprNode):
    def __init__(self, numerator, denominator):
        self.numerator, self.denominator = numerator, denominator

    def __str__(self):
        return "ArithRem[numerator={}, denominator={}]".format(
            str(self.numerator, str(self.denominator)))


class ArithDivDiv(ExprNode):
    def __init__(self, numerator, denominator):
        self.numerator, self.denominator = numerator, denominator

    def __str__(self):
        return "ArithDivDiv[numerator={}, denominator={}]".format(
            str(self.numerator, str(self.denominator)))
