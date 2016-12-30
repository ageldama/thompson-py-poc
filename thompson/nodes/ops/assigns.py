# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode


class Assign(ExprNode):
    def __init__(self, dst, src):
        self.dst, self.src = dst, src

    def __str__(self):
        return "Assign[dst={}, src={}]".format(str(self.dst),
                                               str(self.src))


class AssignUpvar(ExprNode):
    def __init__(self, dst, src):
        self.dst, self.src = dst, src

    def __str__(self):
        return "AssignUpvar[dst={}, src={}]".format(str(self.dst),
                                                    str(self.src))


class AssignGlobal(ExprNode):
    def __init__(self, dst, src):
        self.dst, self.src = dst, src

    def __str__(self):
        return "AssignGlobal[dst={}, src={}]".format(str(self.dst),
                                                     str(self.src))


class Const(ExprNode):
    def __init__(self, dst, src):
        self.dst, self.src = dst, src

    def __str__(self):
        return "Const[dst={}, src={}]".format(str(self.dst),
                                              str(self.src))


class BindingRef(ExprNode):
    def __init__(self, k):
        self.k = k

    def __str__(self):
        return "BindingRef[{}]".format(self.k)


class Let(ExprNode):
    def __init__(self, exprs, body):
        self.exprs = exprs
        self.body = body

    def __str__(self):
        return "Let[{}, {}]".format(to_joined_strs(self.exprs),
                                    str(self.body))

