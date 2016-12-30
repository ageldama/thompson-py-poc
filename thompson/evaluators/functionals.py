# -*- coding: utf-8; -*-
from thompson.evaluators.evaluator import Evaluator
from thompson.evaluators.utils import gimme_str_anyway, evaluate
from thompson.nodes.literals import NilConst, BoolVal, StringVal
from thompson.nodes.literals import NumberVal, NullVal
from thompson.nodes.literals import FunctionParamVal, FunctionVal
from thompson.nodes.literals import MappedVal, MappedFunctionVal
from thompson.nodes.literals import NoWrappingMappedFunctionVal
from thompson.context import Binding, Context


class FunctionValEvaluator(Evaluator):
    def eval(self, context, node):
        assert isinstance(node.params, (list, tuple,))
        for param in node.params:
            assert isinstance(param, FunctionParamVal)
        if node.binding == NilConst:
            # make closure for func-val.
            node.binding = Binding(context.binding)
        return node


class FunctionParamValEvaluator(Evaluator):
    def eval(self, context, node):
        if isinstance(node.name, str):
            return node
        else:
            return FunctionParamVal(
                gimme_str_anyway(context, node.name))


class FuncallEvaluator(Evaluator):
    def _check_arity(self, fun, given_params):
        fun_params = fun.params
        fun_arity = len(fun_params)
        params_len = len(given_params)
        assert fun_arity == params_len

    def _bind_params(self, context, fun, given_params):
        b = fun.binding
        for (fun_param, param_val) in zip(fun.params, given_params):
            k = evaluate(context, fun_param).name
            v = evaluate(context, param_val)
            b.set(k, v)

    def _unwrap_param(self, param):
        if isinstance(param, (BoolVal, StringVal, NumberVal,)):
            return param.get()
        elif isinstance(param, NullVal):
            return None
        elif isinstance(param, MappedVal):
            return param.v
        else:
            return param

    def _unwrap_params(self, context, params):
        return [self._unwrap_param(evaluate(context, p)) for p in params]

    def _wrap_result(self, v):
        if isinstance(v, bool):
            return BoolVal(v)
        elif isinstance(v, (int, float,)):
            return NumberVal(v)
        elif isinstance(v, str):
            return StringVal(v)
        elif v is None:
            return NilConst
        else:
            return MappedVal(v)

    def eval(self, context, node):
        fun = evaluate(context, node.fun)
        if isinstance(fun, FunctionVal):
            self._check_arity(fun, node.params)
            self._bind_params(context, fun, node.params)
            c = Context(fun.binding)
            return evaluate(c, fun.body)
        elif isinstance(fun, NoWrappingMappedFunctionVal):
            return fun.f(*node.params)
        elif isinstance(fun, MappedFunctionVal):
            p = self._unwrap_params(context, node.params)
            return self._wrap_result(fun.f(*p))
        else:
            raise NotImplementedError()


class MappedValEvaluator(Evaluator):
    def eval(self, context, node):
        return node  # simply do nothing.


class MappedFunctionValEvaluator(Evaluator):
    def eval(self, context, node):
        return node  # also does nothing.
