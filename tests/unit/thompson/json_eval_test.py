# -*- coding: utf-8; -*-
from pytest import fixture
from thompson.json_eval import evaluate_json_file
from thompson.nodes.literals import NumberVal


json_filename_and_result_alist = [
    ['simple_add.json', NumberVal(42)],
]


@fixture(params=[i for i in json_filename_and_result_alist],
         ids=[i[0] for i in json_filename_and_result_alist])
def json_filename_and_result(test_data_path, request):
    return (test_data_path / request.param[0], request.param[1])


def test_eval_json_file(empty_context, json_filename_and_result):
    json_filename, expectation = json_filename_and_result
    assert json_filename.exists()
    with json_filename.open('r') as f:
        result = evaluate_json_file(empty_context, f)
        assert result == expectation
