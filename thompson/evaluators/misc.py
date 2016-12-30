# -*- coding: utf-8; -*-
from thompson.evaluators.evaluator import Evaluator
from thompson.nodes.ops import Pass
from thompson.nodes.literals import NilConst


class PassEvaluator(Evaluator):
    def eval(self, context, node):
        assert isinstance(node, Pass)
        return NilConst
