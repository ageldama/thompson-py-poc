# -*- coding: utf-8; -*-
from abc import abstractmethod
from thompson.literals import LiteralNode, NilConst, NullVal, BoolVal
from thompson.literals import FunctionVal, FunctionParamVal
from thompson.literals import NumberVal, StringVal
from thompson.literals import MappedVal, MappedFunctionVal
from thompson.literals import NoWrappingMappedFunctionVal
from thompson.bindings import Binding
from thompson.context import Context
from thompson.builtin_operators import Pass, LogOr, LogAnd, LogNot
from thompson.builtin_operators import ArithAdd, ArithSub
from thompson.builtin_operators import ArithDiv, ArithDivDiv, ArithRem
from thompson.builtin_operators import ArithMult, ArithMultMult
from thompson.builtin_operators import ComparLt, ComparLe, ComparGt, ComparGe
from thompson.builtin_operators import Equal, NotEqual
from thompson.builtin_operators import IsNotNull, IsNull
from thompson.builtin_operators import BindingRef
from thompson.builtin_operators import Assign, AssignGlobal, AssignUpvar
from thompson.builtin_operators import Prog1, ProgN, ParProg
from thompson.builtin_operators import IfThenElse, When, Unless
from thompson.builtin_operators import CaseElse, CondElse
from thompson.builtin_operators import Funcall
from thompson.builtin_operators import Const, Let


def find_evaluator(context, node):
    for (types, evaluator) in __evaluators__:
        if isinstance(node, types):
            return evaluator
    raise ValueError("No matching evaluator for {}".format(str(node)))


def evaluate(context, node):
    """evaluate a node"""
    evaluator = find_evaluator(context, node)
    return evaluator.eval(context, node)


class Evaluator(object):
    @abstractmethod
    def eval(self, context, node):
        pass


class LiteralEvaluator(Evaluator):
    def eval(self, context, node):
        assert isinstance(node, LiteralNode)
        if node is NilConst or isinstance(node, NullVal):
            return NilConst
        else:
            return node


class PassEvaluator(Evaluator):
    def eval(self, context, node):
        assert isinstance(node, Pass)
        return NilConst


def eval_and_type_check(context, node, type_pred):
    node_ = evaluate(context, node)
    assert isinstance(node_, type_pred)
    return node_


class LogAndEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, BoolVal)
        b_ = eval_and_type_check(context, node.b, BoolVal)
        return BoolVal(a_.get() and b_.get())


class LogOrEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, BoolVal)
        b_ = eval_and_type_check(context, node.b, BoolVal)
        return BoolVal(a_.get() or b_.get())


class LogNotEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, BoolVal)
        return BoolVal(not a_.get())


class ArithAddEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, NumberVal)
        b_ = eval_and_type_check(context, node.b, NumberVal)
        return NumberVal(a_.get() + b_.get())


class ArithSubEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, NumberVal)
        b_ = eval_and_type_check(context, node.b, NumberVal)
        return NumberVal(a_.get() - b_.get())


class ArithMultEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, NumberVal)
        b_ = eval_and_type_check(context, node.b, NumberVal)
        return NumberVal(a_.get() * b_.get())


class ArithMultMultEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, NumberVal)
        nth_ = eval_and_type_check(context, node.nth, NumberVal)
        return NumberVal(a_.get() ** nth_.get())


class ArithDivEvaluator(Evaluator):
    def eval(self, context, node):
        num_ = eval_and_type_check(context, node.numerator, NumberVal)
        denom_ = eval_and_type_check(context, node.denominator, NumberVal)
        return NumberVal(num_.get() / denom_.get())


class ArithRemEvaluator(Evaluator):
    def eval(self, context, node):
        num_ = eval_and_type_check(context, node.numerator, NumberVal)
        denom_ = eval_and_type_check(context, node.denominator, NumberVal)
        return NumberVal(num_.get() % denom_.get())


class ArithDivDivEvaluator(Evaluator):
    def eval(self, context, node):
        num_ = eval_and_type_check(context, node.numerator, NumberVal)
        denom_ = eval_and_type_check(context, node.denominator, NumberVal)
        return NumberVal(num_.get() // denom_.get())


class ComparLtEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, NumberVal)
        b_ = eval_and_type_check(context, node.b, NumberVal)
        return BoolVal(a_.get() < b_.get())


class ComparLeEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, NumberVal)
        b_ = eval_and_type_check(context, node.b, NumberVal)
        return BoolVal(a_.get() <= b_.get())


class ComparGtEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, NumberVal)
        b_ = eval_and_type_check(context, node.b, NumberVal)
        return BoolVal(a_.get() > b_.get())


class ComparGeEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = eval_and_type_check(context, node.a, NumberVal)
        b_ = eval_and_type_check(context, node.b, NumberVal)
        return BoolVal(a_.get() >= b_.get())


class EqualEvaluator(Evaluator):
    def eval(self, context, node):
        allows = (BoolVal, NullVal, StringVal, NumberVal)
        a_ = eval_and_type_check(context, node.a, allows)
        b_ = eval_and_type_check(context, node.b, allows)
        if type(a_) != type(b_):
            return BoolVal(False)
        if isinstance(a_, NullVal) and isinstance(b_, NullVal):
            return BoolVal(True)
        else:
            return BoolVal(a_.get() == b_.get())


class NotEqualEvaluator(EqualEvaluator):
    def eval(self, context, node):
        return BoolVal(not super().eval(context, node).get())


class IsNullEvaluator(Evaluator):
    def eval(self, context, node):
        a_ = evaluate(context, node.a)
        return BoolVal(isinstance(a_, NullVal))


class IsNotNullEvaluator(IsNullEvaluator):
    def eval(self, context, node):
        return BoolVal(not super().eval(context, node).get())


def gimme_str_anyway(context, node):
    if isinstance(node, str):
        return node
    elif isinstance(node, (StringVal, NumberVal,)):
        k = evaluate(context, node)
        return str(k.get())
    else:
        return str(node)


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


class Prog1_Evaluator(Evaluator):
    def eval(self, context, node):
        if len(node.exprs) == 0:
            return NilConst
        result = evaluate(context, node.exprs[0])
        for i in node.exprs[1:]:
            evaluate(context, i)
        return result


class ProgN_Evaluator(Evaluator):
    def eval(self, context, node):
        if len(node.exprs) == 0:
            return NilConst
        result = None
        for i in node.exprs:
            result = evaluate(context, i)
        return result


class ParProg_Evaluator(ProgN_Evaluator):
    def eval(self, context, node):
        super().eval(context, node)
        return NilConst


def is_kinda_null(v):
    return v is None or NilConst == v


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


__evaluators__ = (
    # NOTE: `FunctionVal` should be before of `LiteralNode`.
    # NOTE: (Due to it is a subtype of `LiteralNode`.)
    (FunctionParamVal, FunctionParamValEvaluator()),
    (FunctionVal, FunctionValEvaluator()),
    (MappedVal, MappedValEvaluator()),
    (MappedFunctionVal, MappedFunctionValEvaluator()),
    (NoWrappingMappedFunctionVal, MappedFunctionValEvaluator()),
    (LiteralNode, LiteralEvaluator()),
    (LogOr, LogOrEvaluator()),
    (LogAnd, LogAndEvaluator()),
    (LogNot, LogNotEvaluator()),
    (ArithAdd, ArithAddEvaluator()),
    (ArithSub, ArithSubEvaluator()),
    (ArithMult, ArithMultEvaluator()),
    (ArithMultMult, ArithMultMultEvaluator()),
    (ArithRem, ArithRemEvaluator()),
    (ArithDiv, ArithDivEvaluator()),
    (ArithDivDiv, ArithDivDivEvaluator()),
    (ComparLt, ComparLtEvaluator()),
    (ComparLe, ComparLeEvaluator()),
    (ComparGe, ComparGeEvaluator()),
    (ComparGt, ComparGtEvaluator()),
    (Equal, EqualEvaluator()),
    (NotEqual, NotEqualEvaluator()),
    (IsNull, IsNullEvaluator()),
    (IsNotNull, IsNotNullEvaluator()),
    (Assign, AssignEvaluator()),
    (AssignUpvar, AssignUpvarEvaluator()),
    (AssignGlobal, AssignGlobalEvaluator()),
    (BindingRef, BindingRefEvaluator()),
    (Prog1, Prog1_Evaluator()),
    (ProgN, ProgN_Evaluator()),
    (ParProg, ParProg_Evaluator()),
    (IfThenElse, IfThenElseEvaluator()),
    (When, WhenEvaluator()),
    (Unless, UnlessEvaluator()),
    (CaseElse, CaseElseEvaluator()),
    (CondElse, CondElseEvaluator()),
    (Funcall, FuncallEvaluator()),
    (Pass, PassEvaluator()),
    (Const, ConstEvaluator()),
    (Let, LetEvaluator()),
)
