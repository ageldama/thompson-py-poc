# -*- coding: utf-8; -*-
from pytest import fixture
from pathlib import Path
from sexpr import parse_file, Atom, dumps, parse


fn_and_expects = [
    ('comments.sexpr', None),
    ('atom1.sexpr', Atom('foo')),
    ('literals1.sexpr',
     [Atom('example'), 12345, 42, 3.14, 0, -123, -42.3,
      "foo", "bar", "SpamEggs", True, False, None]),
    ('nested_list.sexpr',
     [Atom('foo'), [Atom('bar'), ["spam", "eggs"], 42], True]),
]


@fixture(params=[(i[0], i[1]) for i in fn_and_expects],
         ids=[i[0] for i in fn_and_expects])
def sexpr_path_and_expect(test_data_path, request):
    return (test_data_path / request.param[0], request.param[1])


def test_sexpr_fixture_data(sexpr_path_and_expect):
    sexpr_path, expect = sexpr_path_and_expect
    assert isinstance(sexpr_path, Path)
    assert sexpr_path.absolute()
    assert sexpr_path.exists()


def test_parser(sexpr_path_and_expect):
    sexpr_path, expect = sexpr_path_and_expect
    result = None
    with sexpr_path.open('r') as f:
        result = parse_file(f)
    assert result == expect


def test_dumps(sexpr_path_and_expect):
    sexpr_path, expect = sexpr_path_and_expect
    assert expect == parse(dumps(expect))
