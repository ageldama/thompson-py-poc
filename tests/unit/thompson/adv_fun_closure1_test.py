# -*- coding: utf-8; -*-
import thompson.evaluators.registry  # noqa
from thompson.nodes.literals import NumberVal
from thompson.nodes.literals import FunctionParamVal, FunctionVal
from thompson.nodes.ops import Assign, AssignGlobal
from thompson.nodes.ops import Funcall
from thompson.nodes.ops import Let, Pass, ProgN
from thompson.nodes.ops import ArithAdd, BindingRef
from thompson.json_encdec import loads
from thompson.json_eval import evaluate_json_file
from thompson.context import Context, Binding
from thompson.app.json_eval import run


def make_expr():
    N = NumberVal
    expr = ProgN([Let([Assign('n', N(42)),
                       AssignGlobal('inc',
                                    FunctionVal([FunctionParamVal('x')],
                                                ArithAdd([BindingRef('x'),
                                                          BindingRef('n')])))],
                  Pass()),
                  Funcall(BindingRef('inc'), [N(42)])])
    return expr


def test_closure1(empty_context_eval):
    result = empty_context_eval(make_expr())
    assert result == NumberVal(84)


def test_read_json(test_data_path):
    fn = test_data_path / 'closure1.json'
    with fn.open('r') as f:
        expr = loads(f.read())
        expect = make_expr()
        expr == expect


def test_eval_json(test_data_path):
    fn = test_data_path / 'closure1.json'
    with fn.open('r') as f:
        result = evaluate_json_file(Context(Binding()), f)
        assert result == NumberVal(84)


def test_eval_json_with_app(test_data_path):
    fn = test_data_path / 'closure1.json'
    result = run(fn)
    assert result == NumberVal(84)


def test_run_json_counter(test_data_path):
    fn = test_data_path / 'closure_counter.json'
    from thompson.app.json_eval import run
    result = run(fn)
    assert result == NumberVal(3)


def test_run_json_make_incx(test_data_path):
    fn = test_data_path / 'closure_make_incx.json'
    from thompson.app.json_eval import run
    result = run(fn)
    assert result == NumberVal(43)


def test_run_json_compose(test_data_path):
    fn = test_data_path / 'closure_compose.json'
    from thompson.app.json_eval import run
    result = run(fn)
    assert result == NumberVal(9)
