# -*- coding: utf-8; -*-
from thompson.nodes.literals import LiteralNode, NilConst, NullVal
from thompson.evaluators.evaluator import Evaluator


class LiteralEvaluator(Evaluator):
    def eval(self, context, node):
        assert isinstance(node, LiteralNode)
        if node is NilConst or isinstance(node, NullVal):
            return NilConst
        else:
            return node
