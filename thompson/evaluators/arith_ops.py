# -*- coding: utf-8; -*-
from thompson.evaluators.evaluator import Evaluator
from thompson.nodes.literals import NumberVal
from operator import add, sub, mul, pow, truediv, floordiv, imod
from thompson.evaluators.params import accum_params


class ArithAddEvaluator(Evaluator):
    def eval(self, context, node):
        return accum_params(context, add, node.params, NumberVal)


class ArithSubEvaluator(Evaluator):
    def eval(self, context, node):
        return accum_params(context, sub, node.params, NumberVal)


class ArithMultEvaluator(Evaluator):
    def eval(self, context, node):
        return accum_params(context, mul, node.params, NumberVal)


class ArithMultMultEvaluator(Evaluator):
    def eval(self, context, node):
        return accum_params(context, pow, node.params, NumberVal)


class ArithDivEvaluator(Evaluator):
    def eval(self, context, node):
        return accum_params(context, truediv, node.params, NumberVal)


class ArithRemEvaluator(Evaluator):
    def eval(self, context, node):
        return accum_params(context, imod, node.params, NumberVal)


class ArithDivDivEvaluator(Evaluator):
    def eval(self, context, node):
        return accum_params(context, floordiv, node.params, NumberVal)
