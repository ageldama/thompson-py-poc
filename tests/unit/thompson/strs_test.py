# -*- coding: utf-8; -*-
from thompson.strs import to_joined_strs


def test_to_joined_strs():
    assert to_joined_strs((1, 2, 3,)) == "1,2,3"
    assert to_joined_strs((1, 2, 3,), '| ') == '1| 2| 3'
    assert to_joined_strs((), 'dhjehjeqhjkeqjk') == ''
