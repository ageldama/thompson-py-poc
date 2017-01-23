# -*- coding: utf-8; -*-
from thompson.evaluators.evaluator import Evaluator
from thompson.evaluators.utils import eval_and_type_check
from thompson.nodes.literals import NumberVal, BoolVal
from operator import lt, le, gt, ge


def _cmp_all(context, params, op):
    tnfs = []
    if len(params) < 2:
        return False
    else:
        for i in range(len(params) - 1):
            x, y = params[i], params[i + 1]
            x_ = eval_and_type_check(context, x, NumberVal)
            y_ = eval_and_type_check(context, y, NumberVal)
            tnfs.append(op(x_.get(), y_.get()))
    return BoolVal(all(tnfs))


class ComparLtEvaluator(Evaluator):
    def eval(self, context, node):
        return _cmp_all(context, node.params, lt)


class ComparLeEvaluator(Evaluator):
    def eval(self, context, node):
        return _cmp_all(context, node.params, le)


class ComparGtEvaluator(Evaluator):
    def eval(self, context, node):
        return _cmp_all(context, node.params, gt)


class ComparGeEvaluator(Evaluator):
    def eval(self, context, node):
        return _cmp_all(context, node.params, ge)
