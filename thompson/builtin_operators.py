# -*- coding: utf-8; -*-

from thompson.nodes import Node
from thompson.strs import to_joined_strs
from abc import abstractmethod


class ExprNode(Node):
    @abstractmethod
    def __str__(self):
        pass


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


class Pass(ExprNode):
    def __str__(self):
        return "Pass"


class LogAnd(ExprNode):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __str__(self):
        return "LogAnd[{}, {}]".format(str(self.a), str(self.b))


class LogOr(ExprNode):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __str__(self):
        return "LogOr[{}, {}]".format(str(self.a), str(self.b))


class LogNot(ExprNode):
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return "LogNot[{}]".format(str(self.a))


class ArithAdd(ExprNode):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __str__(self):
        return "ArithAdd[{}, {}]".format(str(self.a), str(self.b))


class ArithSub(ExprNode):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __str__(self):
        return "ArithSub[{}, {}]".format(str(self.a), str(self.b))


class ArithMult(ExprNode):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __str__(self):
        return "ArithMult[{}, {}]".format(str(self.a), str(self.b))


class ArithMultMult(ExprNode):
    def __init__(self, a, nth):
        self.a, self.nth = a, nth

    def __str__(self):
        return "ArithMultMult[{}, nth={}]".format(str(self.a), str(self.nth))


class ArithDiv(ExprNode):
    def __init__(self, numerator, denominator):
        self.numerator, self.denominator = numerator, denominator

    def __str__(self):
        return "ArithDiv[numerator={}, denominator={}]".format(
            str(self.numerator, str(self.denominator)))


class ArithRem(ExprNode):
    def __init__(self, numerator, denominator):
        self.numerator, self.denominator = numerator, denominator

    def __str__(self):
        return "ArithRem[numerator={}, denominator={}]".format(
            str(self.numerator, str(self.denominator)))


class ArithDivDiv(ExprNode):
    def __init__(self, numerator, denominator):
        self.numerator, self.denominator = numerator, denominator

    def __str__(self):
        return "ArithDivDiv[numerator={}, denominator={}]".format(
            str(self.numerator, str(self.denominator)))


class ComparLt(ExprNode):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __str__(self):
        return "ComparLt[{}, {}]".format(str(self.a), str(self.b))


class ComparLe(ExprNode):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __str__(self):
        return "ComparLe[{}, {}]".format(str(self.a), str(self.b))


class ComparGt(ExprNode):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __str__(self):
        return "ComparGt[{}, {}]".format(str(self.a), str(self.b))


class ComparGe(ExprNode):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __str__(self):
        return "ComparGe[{}, {}]".format(str(self.a), str(self.b))


class Equal(ExprNode):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __str__(self):
        return "Equal[{}, {}]".format(str(self.a), str(self.b))


class NotEqual(ExprNode):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __str__(self):
        return "NotEqual[{}, {}]".format(str(self.a), str(self.b))


class IsNull(ExprNode):
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return "IsNull[{}]".format(str(self.a))


class IsNotNull(ExprNode):
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return "IsNotNull[{}]".format(str(self.a))


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


class BindingRef(Node):
    def __init__(self, k):
        self.k = k

    def __str__(self):
        return "BindingRef[{}]".format(self.k)


class Funcall(ExprNode):
    def __init__(self, fun, params):
        self.fun = fun
        self.params = params

    def __str__(self):
        return "Funcall[{}, ({})]".format(self.fun,
                                          to_joined_strs(self.params))


class Let(ExprNode):
    def __init__(self, exprs, body):
        self.exprs = exprs
        self.body = body

    def __str__(self):
        return "Let[{}, {}]".format(to_joined_strs(self.exprs),
                                    str(self.body))
