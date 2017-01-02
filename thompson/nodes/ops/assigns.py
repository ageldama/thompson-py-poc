# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode
from thompson.strs import to_joined_strs
from typing import Union


class Assign(ExprNode):
    def __init__(self, dst: Union['StringVal', str],
                 src: 'Evaluatable') -> None:
        self.dst, self.src = dst, src

    def __str__(self) -> str:
        return "Assign[dst={}, src={}]".format(str(self.dst),
                                               str(self.src))

    def __eq__(self, other) -> bool:
        if not isinstance(other, Assign):
            return False
        else:
            return self.dst == other.dst \
                and self.src == other.src


class AssignUpvar(ExprNode):
    def __init__(self, dst: Union['StringVal', str],
                 src: 'Evaluatable') -> None:
        self.dst, self.src = dst, src

    def __str__(self) -> str:
        return "AssignUpvar[dst={}, src={}]".format(str(self.dst),
                                                    str(self.src))

    def __eq__(self, other) -> bool:
        if not isinstance(other, AssignUpvar):
            return False
        else:
            return self.dst == other.dst \
                and self.src == other.src


class AssignGlobal(ExprNode):
    def __init__(self, dst: Union['StringVal', str],
                 src: 'Evaluatable') -> None:
        self.dst, self.src = dst, src

    def __str__(self) -> str:
        return "AssignGlobal[dst={}, src={}]".format(str(self.dst),
                                                     str(self.src))

    def __eq__(self, other) -> bool:
        if not isinstance(other, AssignGlobal):
            return False
        else:
            return self.dst == other.dst \
                and self.src == other.src


class Const(ExprNode):
    def __init__(self, dst: Union['StringVal', str],
                 src: 'Evaluatable') -> None:
        self.dst, self.src = dst, src

    def __str__(self) -> str:
        return "Const[dst={}, src={}]".format(str(self.dst),
                                              str(self.src))

    def __eq__(self, other) -> bool:
        if not isinstance(other, Const):
            return False
        else:
            return self.dst == other.dst \
                and self.src == other.src


class BindingRef(ExprNode):
    def __init__(self, k: Union['StringVal', str]) -> None:
        self.k = k

    def __str__(self) -> str:
        return "BindingRef[{}]".format(self.k)

    def __eq__(self, other) -> bool:
        if not isinstance(other, BindingRef):
            return False
        else:
            return self.k == other.k


class Let(ExprNode):
    def __init__(self,
                 exprs: Union[Assign, Const, AssignUpvar, AssignGlobal],
                 body: 'Evaluatable') -> None:
        self.exprs = exprs
        self.body = body

    def __str__(self) -> str:
        return "Let[{}, {}]".format(to_joined_strs(self.exprs),
                                    str(self.body))

    def __eq__(self, other) -> bool:
        if not isinstance(other, Let):
            return False
        else:
            return self.exprs == other.exprs \
                and self.body == other.body
