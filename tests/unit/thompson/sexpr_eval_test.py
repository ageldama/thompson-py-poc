# -*- coding: utf-8; -*-
import thompson.evaluators.registry  # noqa
from thompson.sexprs.eval import evaluate_file
from thompson.context import Context, Binding
from thompson.nodes.literals import NumberVal


def test_eval_compose(test_data_path):
    b = Binding()
    b.set('foo', 42)
    c = Context(b)
    fn = test_data_path / 'closure_compose.sexpr'
    with fn.open('r') as f:
        result = evaluate_file(f, c)
        assert result == NumberVal(9)
