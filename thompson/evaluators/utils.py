# -*- coding: utf-8; -*-
from thompson.nodes.literals import NumberVal, StringVal
from thompson.nodes.literals import NilConst
from typing import Union


__evaluators__ = []


def append_evaluator(type_pred,
                     evaluator: 'Evaluator') -> None:
    __evaluators__.append((type_pred, evaluator,))


def find_evaluator(context: 'Context',
                   node: 'Evaluatable') -> 'Evaluator':
    for (types, evaluator) in __evaluators__:
        if isinstance(node, types):
            return evaluator
    raise ValueError("No matching evaluator for {} in {}"
                     .format(str(node), str(__evaluators__)))


def evaluate(context: 'Context',
             node: 'Evaluatable') -> 'LiteralNode':
    """evaluate a node"""
    evaluator = find_evaluator(context, node)
    return evaluator.eval(context, node)


def eval_and_type_check(context: 'Context',
                        node: 'Evaluatable',
                        type_pred) -> 'LiteralNode':
    node_ = evaluate(context, node)
    assert isinstance(node_, type_pred)
    return node_


def gimme_str_anyway(context: 'Context',
                     node: 'Evaluatable') -> str:
    if isinstance(node, str):
        return node
    elif isinstance(node, (StringVal, NumberVal,)):
        k = evaluate(context, node)
        return str(k.get())
    else:
        return str(node)


def is_kinda_null(v: Union[None, 'LiteralNode']) -> bool:
    return v is None or NilConst == v
