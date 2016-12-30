# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode


class Pass(ExprNode):
    def __str__(self):
        return "Pass"


class Funcall(ExprNode):
    def __init__(self, fun, params):
        self.fun = fun
        self.params = params

    def __str__(self):
        return "Funcall[{}, ({})]".format(self.fun,
                                          to_joined_strs(self.params))
