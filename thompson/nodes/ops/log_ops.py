# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode


class LogAnd(ExprNode):
    def __init__(self,
                 a: 'Evaluatable',
                 b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "LogAnd[{}, {}]".format(str(self.a), str(self.b))


class LogOr(ExprNode):
    def __init__(self,
                 a: 'Evaluatable',
                 b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "LogOr[{}, {}]".format(str(self.a), str(self.b))


class LogNot(ExprNode):
    def __init__(self, a: 'Evaluatable') -> None:
        self.a = a

    def __str__(self) -> str:
        return "LogNot[{}]".format(str(self.a))
