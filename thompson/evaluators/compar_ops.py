# -*- coding: utf-8; -*-
from thompson.evaluators.evaluator import Evaluator
from thompson.evaluators.utils import eval_and_type_check
from thompson.nodes.literals import NumberVal, BoolVal


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
