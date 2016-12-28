# -*- coding: utf-8; -*-
from abc import abstractmethod
from thompson.literals import LiteralNode, NilConst, NullVal, BoolVal
from thompson.literals import NumberVal, StringVal
from thompson.builtin_operators import ExprNode
from thompson.builtin_operators import Pass, LogOr, LogAnd, LogNot
from thompson.builtin_operators import ArithPlus, ArithMinus
from thompson.builtin_operators import ArithDiv, ArithDivDiv, ArithRem
from thompson.builtin_operators import ArithMult, ArithMultMult
from thompson.builtin_operators import ComparLt, ComparLe, ComparGt, ComparGe
from thompson.builtin_operators import Equal, NotEqual
from thompson.builtin_operators import IsNotNull, IsNull
from thompson.builtin_operators import BindingRef
from thompson.builtin_operators import Assign, AssignGlobal, AssignUpvar
from thompson.builtin_operators import Prog1, ProgN, ParProg
from thompson.builtin_operators import IfThenElse, When, Unless


def find_evaluator(context, node):
    for (types, evaluator) in __evaluators__.items():
        if isinstance(node, types):
            return evaluator
    raise ValueError("No matching evaluator for {}".format(str(node)))


def evaluate(context, node):
    """evaluate a node"""
    evaluator = find_evaluator(context, node)
    return evaluator.eval(context, node)


class Evaluator(object):
    @abstractmethod
    def eval(self, context, node):
        pass


class LiteralEvaluator(Evaluator):
    def eval(self, context, node):
        assert isinstance(node, LiteralNode)
        if node is NilConst or isinstance(node, NullVal):
            return NilConst
        else:
            return node


class PassEvaluator(Evaluator):
    def eval(self, context, node):
        assert isinstance(node, Pass)
        return NilConst


def eval_and_type_check(context, node, type_pred):
    node_ = evaluate(context, node)
    assert isinstance(node_, type_pred)
    return node_


class LogAndEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, BoolVal)
        b_ = eval_and_type_check(context, node.b, BoolVal)
        return BoolVal(a_.get() and b_.get())


class LogOrEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, BoolVal)
        b_ = eval_and_type_check(context, node.b, BoolVal)
        return BoolVal(a_.get() or b_.get())


class LogNotEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, BoolVal)
        return BoolVal(not a_.get())


class ArithPlusEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, NumberVal)
        b_ = eval_and_type_check(context, node.b, NumberVal)
        return NumberVal(a_.get() + b_.get())


class ArithMinusEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, NumberVal)
        b_ = eval_and_type_check(context, node.b, NumberVal)
        return NumberVal(a_.get() - b_.get())


class ArithMultEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, NumberVal)
        b_ = eval_and_type_check(context, node.b, NumberVal)
        return NumberVal(a_.get() * b_.get())


class ArithMultMultEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, NumberVal)
        nth_ = eval_and_type_check(context, node.nth, NumberVal)
        return NumberVal(a_.get() ** nth_.get())


class ArithDivEvaluator(Evaluator):
    def eval(self, context, node):
        num_ = eval_and_type_check(context, node.numerator, NumberVal)
        denom_ = eval_and_type_check(context, node.denominator, NumberVal)
        return NumberVal(num_.get() / denom_.get())


class ArithRemEvaluator(Evaluator):
    def eval(self, context, node):
        num_ = eval_and_type_check(context, node.numerator, NumberVal)
        denom_ = eval_and_type_check(context, node.denominator, NumberVal)
        return NumberVal(num_.get() % denom_.get())


class ArithDivDivEvaluator(Evaluator):
    def eval(self, context, node):
        num_ = eval_and_type_check(context, node.numerator, NumberVal)
        denom_ = eval_and_type_check(context, node.denominator, NumberVal)
        return NumberVal(num_.get() // denom_.get())


class ComparLtEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, NumberVal)
        b_ = eval_and_type_check(context, node.b, NumberVal)
        return BoolVal(a_.get() < b_.get())


class ComparLeEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, NumberVal)
        b_ = eval_and_type_check(context, node.b, NumberVal)
        return BoolVal(a_.get() <= b_.get())


class ComparGtEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, NumberVal)
        b_ = eval_and_type_check(context, node.b, NumberVal)
        return BoolVal(a_.get() > b_.get())


class ComparGeEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, NumberVal)
        b_ = eval_and_type_check(context, node.b, NumberVal)
        return BoolVal(a_.get() >= b_.get())


class EqualEvaluator(Evaluator):
    def eval(self, context, node):
        allows = (BoolVal, NullVal, StringVal, NumberVal)
        a_ = eval_and_type_check(context, node.a, allows)
        b_ = eval_and_type_check(context, node.b, allows)
        if type(a_) != type(b_):
            return BoolVal(False)
        if isinstance(a_, NullVal) and isinstance(b_, NullVal):
            return BoolVal(True)
        else:
            return BoolVal(a_.get() == b_.get())


class NotEqualEvaluator(EqualEvaluator):
    def eval(self, context, node):
        return BoolVal(not super().eval(context, node).get())


class IsNullEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = evaluate(context, node.a)
        return BoolVal(isinstance(a_, NullVal))


class IsNotNullEvaluator(IsNullEvaluator):
    def eval(self, context, node):
        return BoolVal(not super().eval(context, node).get())


def gimme_str_anyway(context, node):
    if isinstance(node, ExprNode):
        k = evaluate(context, node)
        return str(k.get())
    else:
        return str(node)


class BindingRefEvaluator(Evaluator):
    def eval(self, context, node):
        k = gimme_str_anyway(context, node.k)
        return context.binding.get(k)


class AssignEvaluator(Evaluator):
    def eval(self, context, node):
        k = gimme_str_anyway(context, node.dst)
        v = evaluate(context, node.src)
        context.binding.set(k, v)
        return v


class AssignUpvarEvaluator(Evaluator):
    def eval(self, context, node):
        k = gimme_str_anyway(context, node.dst)
        v = evaluate(context, node.src)
        context.binding.set_uplevel(k, v)
        return v


class AssignGlobalEvaluator(Evaluator):
    def eval(self, context, node):
        k = gimme_str_anyway(context, node.dst)
        v = evaluate(context, node.src)
        context.binding.set_global(k, v)
        return v


class Prog1_Evaluator(Evaluator):
    def eval(self, context, node):
        if len(node.exprs) == 0:
            return NilConst
        result = evaluate(context, node.exprs[0])
        for i in node.exprs[1:]:
            evaluate(context, i)
        return result


class ProgN_Evaluator(Evaluator):
    def eval(self, context, node):
        if len(node.exprs) == 0:
            return NilConst
        result = None
        for i in node.exprs:
            result = evaluate(context, i)
        return result


class ParProg_Evaluator(ProgN_Evaluator):
    def eval(self, context, node):
        super().eval(context, node)
        return NilConst


def is_kinda_null(v):
    return v is None or v == NilConst


class IfThenElseEvaluator(Evaluator):
    def eval(self, context, node, skip_else=False, negate_cond=False):
        cond_ = evaluate(context, node.cond).get()
        if negate_cond:
            cond_ = not cond_
        if cond_:
            return evaluate(context, node.then_clause)
        else:
            if not is_kinda_null(node.else_clause) and not skip_else:
                return evaluate(context, node.else_clause)
            else:
                return NilConst


class WhenEvaluator(IfThenElseEvaluator):
    def eval(self, context, node):
        return super().eval(context, node, skip_else=True)


class UnlessEvaluator(IfThenElseEvaluator):
    def eval(self, context, node):
        return super().eval(context, node, skip_else=True, negate_cond=True)


# TODO: CaseElse
# TODO: CondElse

# TODO: Const
# TODO: funcall


__evaluators__ = {
    (LiteralNode,): LiteralEvaluator(),
    (LogOr,): LogOrEvaluator(),
    (LogAnd,): LogAndEvaluator(),
    (LogNot,): LogNotEvaluator(),
    (ArithPlus,): ArithPlusEvaluator(),
    (ArithMinus,): ArithMinusEvaluator(),
    (ArithMult,): ArithMultEvaluator(),
    (ArithMultMult,): ArithMultMultEvaluator(),
    (ArithRem,): ArithRemEvaluator(),
    (ArithDiv,): ArithDivEvaluator(),
    (ArithDivDiv,): ArithDivDivEvaluator(),
    (ComparLt,): ComparLtEvaluator(),
    (ComparLe,): ComparLeEvaluator(),
    (ComparGe,): ComparGeEvaluator(),
    (ComparGt,): ComparGtEvaluator(),
    (Equal,): EqualEvaluator(),
    (NotEqual,): NotEqualEvaluator(),
    (IsNull,): IsNullEvaluator(),
    (IsNotNull,): IsNotNullEvaluator(),
    (Assign,): AssignEvaluator(),
    (AssignUpvar,): AssignUpvarEvaluator(),
    (AssignGlobal,): AssignGlobalEvaluator(),
    (BindingRef,): BindingRefEvaluator(),
    (Prog1,): Prog1_Evaluator(),
    (ProgN,): ProgN_Evaluator(),
    (ParProg,): ParProg_Evaluator(),
    (IfThenElse,): IfThenElseEvaluator(),
    (When,): WhenEvaluator(),
    (Unless,): UnlessEvaluator(),
    (Pass,): PassEvaluator(),
}
