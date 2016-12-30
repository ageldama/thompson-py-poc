# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode
from typing import Union


class LogAnd(ExprNode):
    def __init__(self,
                 a: Union[ExprNode, 'LiteralNode'],
                 b: Union[ExprNode, 'LiteralNode']):
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "LogAnd[{}, {}]".format(str(self.a), str(self.b))


class LogOr(ExprNode):
    def __init__(self,
                 a: Union[ExprNode, 'LiteralNode'],
                 b: Union[ExprNode, 'LiteralNode']):
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "LogOr[{}, {}]".format(str(self.a), str(self.b))


class LogNot(ExprNode):
    def __init__(self, a: Union[ExprNode, 'LiteralNode']):
        self.a = a

    def __str__(self) -> str:
        return "LogNot[{}]".format(str(self.a))
