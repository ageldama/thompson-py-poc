# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode
from thompson.strs import to_joined_strs
from typing import Sequence


class Prog1(ExprNode):
    def __init__(self,
                 exprs: Sequence['thompson.nodes.Evaluatable']) -> None:
        self.exprs = exprs

    def __str__(self) -> str:
        return "Prog1[{}]".format(to_joined_strs(self.exprs))

    def __eq__(self, other) -> bool:
        if not isinstance(other, Prog1):
            return False
        else:
            return self.exprs == other.exprs


class ProgN(ExprNode):
    def __init__(self,
                 exprs: Sequence['Evaluatable']) -> None:
        self.exprs = exprs

    def __str__(self) -> str:
        return "ProgN[{}]".format(to_joined_strs(self.exprs))

    def __eq__(self, other) -> bool:
        if not isinstance(other, ProgN):
            return False
        else:
            return self.exprs == other.exprs


class ParProg(ExprNode):
    def __init__(self, exprs: Sequence['Evaluatable']) -> None:
        self.exprs = exprs

    def __str__(self) -> str:
        return "ParProg[{}]".format(to_joined_strs(self.exprs))

    def __eq__(self, other) -> bool:
        if not isinstance(other, ParProg):
            return False
        else:
            return self.exprs == other.exprs
