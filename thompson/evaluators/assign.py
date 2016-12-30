# -*- coding: utf-8; -*-
from thompson.evaluators.evaluator import Evaluator
from thompson.evaluators.utils import gimme_str_anyway, evaluate
from thompson.nodes.ops import Assign, AssignUpvar, AssignGlobal
from thompson.nodes.ops import Const
from thompson.context import Context, Binding


class BindingRefEvaluator(Evaluator):
    def eval(self, context, node):
        k = gimme_str_anyway(context, node.k)
        return context.binding.get(k)


class AssignEvaluator(Evaluator):
    def eval(self, context, node):
        k = gimme_str_anyway(context, node.dst)
        v = evaluate(context, node.src)
        context.binding.set(k, v)
        return v


class AssignUpvarEvaluator(Evaluator):
    def eval(self, context, node):
        k = gimme_str_anyway(context, node.dst)
        v = evaluate(context, node.src)
        context.binding.set_uplevel(k, v)
        return v


class AssignGlobalEvaluator(Evaluator):
    def eval(self, context, node):
        k = gimme_str_anyway(context, node.dst)
        v = evaluate(context, node.src)
        context.binding.set_global(k, v)
        return v


class ConstEvaluator(Evaluator):
    def eval(self, context, node):
        v = evaluate(context, node.src)
        k = gimme_str_anyway(context, node.dst)
        context.binding.set(k, v, const=True)
        return v


class LetEvaluator(Evaluator):
    def _check_exprs(self, exprs):
        types = (Const, Assign, AssignUpvar, AssignGlobal,)
        for expr in exprs:
            assert isinstance(expr, types)

    def _evals(self, context, exprs):
        for expr in exprs:
            evaluate(context, expr)

    def eval(self, context, node):
        self._check_exprs(node.exprs)
        b2 = Binding(context.binding)
        c2 = Context(b2)
        self._evals(c2, node.exprs)
        return evaluate(c2, node.body)
