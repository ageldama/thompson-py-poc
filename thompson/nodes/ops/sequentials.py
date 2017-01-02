# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode
from thompson.strs import to_joined_strs
from typing import Sequence


class Prog1(ExprNode):
    def __init__(self,
                 exprs: Sequence['Evaluatable']):
        self.exprs = exprs

    def __str__(self) -> str:
        return "Prog1[{}]".format(to_joined_strs(self.exprs))


class ProgN(ExprNode):
    def __init__(self,
                 exprs: Sequence['Evaluatable']):
        self.exprs = exprs

    def __str__(self) -> str:
        return "ProgN[{}]".format(to_joined_strs(self.exprs))


class ParProg(ExprNode):
    def __init__(self, exprs: Sequence['Evaluatable']):
        self.exprs = exprs

    def __str__(self) -> str:
        return "ParProg[{}]".format(to_joined_strs(self.exprs))
