# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode
from thompson.strs import to_joined_strs


class Prog1(ExprNode):
    def __init__(self, exprs):
        self.exprs = exprs

    def __str__(self):
        return "Prog1[{}]".format(to_joined_strs(self.exprs))


class ProgN(ExprNode):
    def __init__(self, exprs):
        self.exprs = exprs

    def __str__(self):
        return "ProgN[{}]".format(to_joined_strs(self.exprs))


class ParProg(ExprNode):
    def __init__(self, exprs):
        self.exprs = exprs

    def __str__(self):
        return "ParProg[{}]".format(to_joined_strs(self.exprs))
