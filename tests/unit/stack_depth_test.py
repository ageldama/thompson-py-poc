# -*- coding: utf-8; -*-
from thompson.literals import NumberVal
from thompson.builtin_operators import ArithAdd
import pytest


@pytest.mark.skip
def test_stack_depth(empty_context_eval):
    E = empty_context_eval
    N = NumberVal
    count = 0
    BASE = ArithAdd(N(1), N(1))
    cur = BASE
    while True:
        try:
            result = E(cur)
            assert result == N(count + 2)
            count = count + 1
            cur = ArithAdd(N(1), cur)
        except:
            break
    print("max = ", count)
    assert None is count
