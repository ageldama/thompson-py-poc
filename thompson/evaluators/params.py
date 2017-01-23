# -*- coding: utf-8; -*-
from thompson.evaluators.utils import eval_and_type_check
from thompson.nodes.literals import NumberVal


def accum_params(context, op, params, val_klass=NumberVal, init_val=0):
    n = init_val
    if len(params) > 0:
        n = eval_and_type_check(context, params[0], val_klass).get()
        for i in params[1:]:
            i_ = eval_and_type_check(context, i, val_klass)
            n = op(n, i_.get())
    return val_klass(n)
