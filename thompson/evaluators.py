# -*- coding: utf-8; -*-
from abc import abstractmethod
from thompson.literals import LiteralNode, NilConst, NullVal, BoolVal
from thompson.literals import NumberVal
from thompson.builtin_operators import Pass, LogOr, LogAnd, LogNot
from thompson.builtin_operators import ArithPlus, ArithMinus
from thompson.builtin_operators import ArithDiv, ArithDivDiv, ArithRem
from thompson.builtin_operators import ArithMult, ArithMultMult
from thompson.builtin_operators import ComparLt, ComparLe, ComparGt, ComparGe


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


# TODO: ComparLt, Le, Gt, Ge

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

# TODO: Equal, NotEqual

# TODO: IsNull, IsNotNull

# TODO: Assign
# TODO: AssignUpvar
# TODO: AssignGlobal
# TODO: Const

# TODO: Prog1
# TODO: ProgN
# TODO: ParProg

# TODO: IfThenElse
# TODO: When
# TODO: Unless
# TODO: CaseElse
# TODO: CondElse

# TODO: funcall

# TODO: binding-ref?


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
    (Pass,): PassEvaluator(),
}
