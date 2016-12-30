# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode
from thompson.strs import to_joined_strs


class IfThenElse(ExprNode):
    def __init__(self, cond, then_clause, else_clause=None):
        self.cond = cond
        self.then_clause = then_clause
        self.else_clause = else_clause

    def __str__(self):
        fmt = "IfThenElse[cond={}, then={}, else={}]"
        return fmt.format(str(self.cond),
                          str(self.then_clause), str(self.else_clause))


class When(ExprNode):
    def __init__(self, cond, then_clause):
        self.cond = cond
        self.then_clause = then_clause

    def __str__(self):
        fmt = "When[cond={}, then={}]"
        return fmt.format(str(self.cond),
                          str(self.then_clause))


class Unless(ExprNode):
    def __init__(self, cond, then_clause):
        self.cond = cond
        self.then_clause = then_clause

    def __str__(self):
        fmt = "Unless[cond={}, then={}]"
        return fmt.format(str(self.cond),
                          str(self.then_clause))


class CaseItem(ExprNode):
    def __init__(self, v, then_clause):
        self.v, self.then_clause = v, then_clause

    def __str__(self):
        return "CaseItem[v={}, then={}]".format(
            str(self.v), str(self.then_clause))


class CaseElse(ExprNode):
    def __init__(self, v, case_items, else_clause=None):
        self.v = v
        self.case_items = case_items
        self.else_clause = else_clause

    def __str__(self):
        return "CaseElse[v={}, cases={}, else={}]".format(
            str(self.v), to_joined_strs(self.case_items),
            str(self.else_clause))


class CondItem(ExprNode):
    def __init__(self, cond, then_clause):
        self.cond = cond
        self.then_clause = then_clause

    def __str__(self):
        return "CondItem[cond={}, then={}]".format(str(self.cond),
                                                   str(self.then_clause))


class CondElse(ExprNode):
    def __init__(self, cond_items, else_clause=None):
        self.cond_items = cond_items
        self.else_clause = else_clause

    def __str__(self):
        return "CondElse[conds={}, else={}]".format(
            str(self.cond_items), str(self.else_clause))
