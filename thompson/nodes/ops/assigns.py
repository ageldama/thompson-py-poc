# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode
from thompson.strs import to_joined_strs
from typing import Union


class Assign(ExprNode):
    def __init__(self, dst: Union['StringVal', str],
                 src: Union['LiteralNode', ExprNode]):
        self.dst, self.src = dst, src

    def __str__(self) -> str:
        return "Assign[dst={}, src={}]".format(str(self.dst),
                                               str(self.src))


class AssignUpvar(ExprNode):
    def __init__(self, dst: Union['StringVal', str],
                 src: Union['LiteralNode', ExprNode]):
        self.dst, self.src = dst, src

    def __str__(self) -> str:
        return "AssignUpvar[dst={}, src={}]".format(str(self.dst),
                                                    str(self.src))


class AssignGlobal(ExprNode):
    def __init__(self, dst: Union['StringVal', str],
                 src: Union['LiteralNode', ExprNode]):
        self.dst, self.src = dst, src

    def __str__(self) -> str:
        return "AssignGlobal[dst={}, src={}]".format(str(self.dst),
                                                     str(self.src))


class Const(ExprNode):
    def __init__(self, dst: Union['StringVal', str],
                 src: Union['LiteralNode', ExprNode]):
        self.dst, self.src = dst, src

    def __str__(self) -> str:
        return "Const[dst={}, src={}]".format(str(self.dst),
                                              str(self.src))


class BindingRef(ExprNode):
    def __init__(self, k: Union['StringVal', str]):
        self.k = k

    def __str__(self) -> str:
        return "BindingRef[{}]".format(self.k)


class Let(ExprNode):
    def __init__(self,
                 exprs: Union[Assign, Const, AssignUpvar, AssignGlobal],
                 body: Union['LiteralNode', ExprNode]):
        self.exprs = exprs
        self.body = body

    def __str__(self) -> str:
        return "Let[{}, {}]".format(to_joined_strs(self.exprs),
                                    str(self.body))