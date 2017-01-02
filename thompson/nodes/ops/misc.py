# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode
from thompson.strs import to_joined_strs
from typing import Sequence, Any


class Pass(ExprNode):
    def __str__(self) -> str:
        return "Pass"


class Funcall(ExprNode):
    def __init__(self,
                 fun: 'Evaluatable',
                 params: Sequence[Any]) -> None:
        self.fun = fun
        self.params = params

    def __str__(self) -> str:
        return "Funcall[{}, ({})]".format(self.fun,
                                          to_joined_strs(self.params))
