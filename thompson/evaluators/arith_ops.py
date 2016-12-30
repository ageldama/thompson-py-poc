# -*- coding: utf-8; -*-
from thompson.evaluators.utils import eval_and_type_check
from thompson.evaluators.evaluator import Evaluator
from thompson.nodes.literals import NumberVal


class ArithAddEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, NumberVal)
        b_ = eval_and_type_check(context, node.b, NumberVal)
        return NumberVal(a_.get() + b_.get())


class ArithSubEvaluator(Evaluator):
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
