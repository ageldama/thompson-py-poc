# -*- coding: utf-8; -*-
from pathlib import Path
from pytest import fixture
from thompson.json_eval import evaluate_json_file
from thompson.nodes.literals import NumberVal


TEST_DATA_PATH = (Path(__file__).parent.parent / 'data')


json_filename_and_result_alist = [
    [(TEST_DATA_PATH / 'simple_add.json'), NumberVal(42)],
]


@fixture(params=[i for i in json_filename_and_result_alist],
         ids=[i[0].name for i in json_filename_and_result_alist])
def json_filename_and_result(request):
    return request.param


def test_eval_json_file(empty_context, json_filename_and_result):
    json_filename, expectation = json_filename_and_result
    assert json_filename.exists()
    with json_filename.open('r') as f:
        result = evaluate_json_file(empty_context, f)
        assert result == expectation
