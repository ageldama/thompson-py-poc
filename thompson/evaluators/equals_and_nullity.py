# -*- coding: utf-8; -*-
from thompson.evaluators.evaluator import Evaluator
from thompson.evaluators.utils import eval_and_type_check, evaluate
from thompson.nodes.literals import BoolVal, StringVal, NumberVal, NullVal
from operator import eq, ne, and_, or_
from functools import reduce


def _accum(context, params, op, reduce_op, init_val):
    allows = (BoolVal, NullVal, StringVal, NumberVal)
    tnfs = []
    for i in range(len(params) - 1):
        a_ = eval_and_type_check(context, params[i], allows)
        b_ = eval_and_type_check(context, params[i + 1], allows)
        tnfs.append(op(a_.get(), b_.get()))
    return BoolVal(reduce(reduce_op, tnfs, init_val))


class EqualEvaluator(Evaluator):
    def eval(self, context, node):
        return _accum(context, node.params, eq, and_, True)


class NotEqualEvaluator(Evaluator):
    def eval(self, context, node):
        return _accum(context, node.params, ne, or_, False)


class IsNullEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = evaluate(context, node.a)
        return BoolVal(isinstance(a_, NullVal))


class IsNotNullEvaluator(IsNullEvaluator):
    def eval(self, context, node):
        return BoolVal(not super().eval(context, node).get())
