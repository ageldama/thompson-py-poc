# -*- coding: utf-8; -*-
from thompson.evaluators.evaluator import Evaluator
from thompson.evaluators.utils import evaluate, is_kinda_null
from thompson.nodes.literals import NilConst, BoolVal


class IfThenElseEvaluator(Evaluator):
    def eval(self, context, node):
        cond_ = evaluate(context, node.cond).get()
        if cond_:
            return evaluate(context, node.then_clause)
        else:
            if not is_kinda_null(node.else_clause):
                return evaluate(context, node.else_clause)
            else:
                return NilConst


class WhenEvaluator(Evaluator):
    def eval(self, context, node):
        cond_ = evaluate(context, node.cond).get()
        if cond_:
            return evaluate(context, node.then_clause)
        else:
            return NilConst


class UnlessEvaluator(Evaluator):
    def eval(self, context, node):
        cond_ = evaluate(context, node.cond).get()
        if not cond_:
            return evaluate(context, node.then_clause)
        else:
            return NilConst


class CaseElseEvaluator(Evaluator):
    def eval(self, context, node):
        v_ = evaluate(context, node.v)
        for case_item in node.case_items:
            other_ = evaluate(context, case_item.v)
            if v_ == other_:
                return evaluate(context, case_item.then_clause)
        if not is_kinda_null(node.else_clause):
            return evaluate(context, node.else_clause)
        else:
            return NilConst


class CondElseEvaluator(Evaluator):
    def eval(self, context, node):
        for cond_item in node.cond_items:
            cond_ = evaluate(context, cond_item.cond)
            if cond_ == BoolVal(True):
                return evaluate(context, cond_item.then_clause)
        if not is_kinda_null(node.else_clause):
            return evaluate(context, node.else_clause)
        else:
            return NilConst
