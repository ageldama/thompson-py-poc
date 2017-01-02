# -*- coding: utf-8; -*-
from thompson.evaluators.evaluator import Evaluator
from thompson.evaluators.utils import evaluate
from thompson.nodes.literals import NilConst


class Prog1_Evaluator(Evaluator):
    def eval(self, context, node: 'Evaluatable') -> 'Evaluatable':
        if len(node.exprs) == 0:
            return NilConst
        result = evaluate(context, node.exprs[0])
        for i in node.exprs[1:]:
            evaluate(context, i)
        return result


class ProgN_Evaluator(Evaluator):
    def eval(self, context, node: 'Evaluatable') -> 'Evaluatable':
        if len(node.exprs) == 0:
            return NilConst
        result = None
        for i in node.exprs:
            result = evaluate(context, i)
        return result


class ParProg_Evaluator(ProgN_Evaluator):
    def eval(self, context, node: 'Evaluatable') -> 'Evaluatable':
        super().eval(context, node)
        return NilConst
