# -*- coding: utf-8; -*-
from thompson.evaluators.utils import eval_and_type_check
from thompson.evaluators.evaluator import Evaluator
from thompson.nodes.literals import BoolVal
from operator import and_, or_
from functools import reduce


def _accum(context, params, op, init_val):
    tnfs = []
    for i in range(len(params) - 1):
        a_ = eval_and_type_check(context, params[i], BoolVal)
        b_ = eval_and_type_check(context, params[i + 1], BoolVal)
        tnfs.append(op(a_.get(), b_.get()))
    return BoolVal(reduce(op, tnfs, init_val))


class LogAndEvaluator(Evaluator):
    def eval(self, context, node):
        return _accum(context, node.params, and_, True)


class LogOrEvaluator(Evaluator):
    def eval(self, context, node):
        return _accum(context, node.params, or_, False)


class LogNotEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, BoolVal)
        return BoolVal(not a_.get())
