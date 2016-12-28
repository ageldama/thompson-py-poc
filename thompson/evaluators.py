# -*- coding: utf-8; -*-
from abc import abstractmethod
from thompson.literals import LiteralNode, NilConst, NullVal, BoolVal
from thompson.builtin_operators import Pass, LogOr, LogAnd, LogNot


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


class LogAndEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = evaluate(context, node.a)
        assert isinstance(a_, BoolVal)
        b_ = evaluate(context, node.b)
        assert isinstance(b_, BoolVal)
        return BoolVal(a_.get() and b_.get())


class LogOrEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = evaluate(context, node.a)
        assert isinstance(a_, BoolVal)
        b_ = evaluate(context, node.b)
        assert isinstance(b_, BoolVal)
        return BoolVal(a_.get() or b_.get())


class LogNotEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = evaluate(context, node.a)
        assert isinstance(a_, BoolVal)
        return BoolVal(not a_.get())


"""
class ArithOpsEvaluator(Evaluator):
    def eval(self, context, node):
        if 
"""
        
# TODO: ArithPlus, ArithMinus,
# TODO: ArithDiv, ArithRem, ArithDivDiv
# TODO: ArithMult, ArithMultMult

# TODO: ComparLt, Le, Gt, Ge

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
    (Pass,): PassEvaluator(),
}
