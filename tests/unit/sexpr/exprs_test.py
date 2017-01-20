# -*- coding: utf-8; -*-
from sexpr import Exprs


def test_exprs_as_a_list():
    exprs = Exprs()
    assert isinstance(exprs, Exprs)
    assert len(exprs) == 0
    exprs.append(42)
    assert len(exprs) == 1
    assert exprs[0] == 42
    exprs.append(1)
    l = [i for i in exprs]
    assert l == [42, 1]
    m = []
    for i in exprs:
        m.append(i)
    assert m == [42, 1]
