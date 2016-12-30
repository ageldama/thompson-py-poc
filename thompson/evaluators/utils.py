# -*- coding: utf-8; -*-
from thompson.nodes.literals import NumberVal, StringVal
from thompson.nodes.literals import NilConst


__evaluators__ = []


def append_evaluator(type_pred, evaluator):
    __evaluators__.append((type_pred, evaluator,))


def find_evaluator(context, node):
    for (types, evaluator) in __evaluators__:
        if isinstance(node, types):
            return evaluator
    raise ValueError("No matching evaluator for {}".format(str(node)))


def evaluate(context, node):
    """evaluate a node"""
    evaluator = find_evaluator(context, node)
    return evaluator.eval(context, node)


def eval_and_type_check(context, node, type_pred):
    node_ = evaluate(context, node)
    assert isinstance(node_, type_pred)
    return node_


def gimme_str_anyway(context, node):
    if isinstance(node, str):
        return node
    elif isinstance(node, (StringVal, NumberVal,)):
        k = evaluate(context, node)
        return str(k.get())
    else:
        return str(node)


def is_kinda_null(v):
    return v is None or NilConst == v
