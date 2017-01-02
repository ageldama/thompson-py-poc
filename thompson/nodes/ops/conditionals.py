# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode, NonExprNode
from thompson.strs import to_joined_strs
from typing import Optional, Sequence


class IfThenElse(ExprNode):
    def __init__(self,
                 cond: 'Evaluatable',
                 then_clause: 'Evaluatable',
                 else_clause: Optional['Evaluatable']=None) -> None:
        self.cond = cond
        self.then_clause = then_clause
        self.else_clause = else_clause

    def __str__(self) -> str:
        fmt = "IfThenElse[cond={}, then={}, else={}]"
        return fmt.format(str(self.cond),
                          str(self.then_clause), str(self.else_clause))


class When(ExprNode):
    def __init__(self,
                 cond: 'Evaluatable',
                 then_clause: 'Evaluatable') -> None:
        self.cond = cond
        self.then_clause = then_clause

    def __str__(self) -> str:
        fmt = "When[cond={}, then={}]"
        return fmt.format(str(self.cond),
                          str(self.then_clause))


class Unless(ExprNode):
    def __init__(self,
                 cond: 'Evaluatable',
                 then_clause: 'Evaluatable') -> None:
        self.cond = cond
        self.then_clause = then_clause

    def __str__(self) -> str:
        fmt = "Unless[cond={}, then={}]"
        return fmt.format(str(self.cond),
                          str(self.then_clause))


class CaseItem(NonExprNode):
    def __init__(self,
                 v: 'Evaluatable',
                 then_clause: 'Evaluatable') -> None:
        self.v, self.then_clause = v, then_clause

    def __str__(self) -> str:
        return "CaseItem[v={}, then={}]".format(
            str(self.v), str(self.then_clause))


class CaseElse(ExprNode):
    def __init__(self,
                 v: 'Evaluatable',
                 case_items: Sequence[CaseItem],
                 else_clause: Optional['Evaluatable']=None) -> None:
        self.v = v
        self.case_items = case_items
        self.else_clause = else_clause

    def __str__(self) -> str:
        return "CaseElse[v={}, cases={}, else={}]".format(
            str(self.v), to_joined_strs(self.case_items),
            str(self.else_clause))


class CondItem(NonExprNode):
    def __init__(self,
                 cond: 'Evaluatable',
                 then_clause: 'Evaluatable') -> None:
        self.cond = cond
        self.then_clause = then_clause

    def __str__(self) -> str:
        return "CondItem[cond={}, then={}]".format(str(self.cond),
                                                   str(self.then_clause))


class CondElse(ExprNode):
    def __init__(self,
                 cond_items: Sequence[CondItem],
                 else_clause: Optional['Evaluatable']=None) -> None:
        self.cond_items = cond_items
        self.else_clause = else_clause

    def __str__(self) -> str:
        return "CondElse[conds={}, else={}]".format(
            str(self.cond_items), str(self.else_clause))
