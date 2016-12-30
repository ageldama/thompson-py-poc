# -*- coding: utf-8; -*-
from thompson.evaluators.utils import eval_and_type_check
from thompson.evaluators.evaluator import Evaluator
from thompson.nodes.literals import BoolVal


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
