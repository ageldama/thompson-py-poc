# -*- coding: utf-8; -*-
from thompson.evaluators.evaluator import Evaluator
from thompson.evaluators.utils import eval_and_type_check, evaluate
from thompson.nodes.literals import BoolVal, StringVal, NumberVal, NullVal


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
