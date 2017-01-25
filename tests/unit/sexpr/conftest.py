# -*- coding: utf-8; -*-
from pytest import fixture
from pathlib import Path


@fixture
def test_data_path() -> Path:
    return (Path(__file__).parent.parent.parent / 'data/sexpr')
