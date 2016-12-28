# -*- coding: utf-8; -*-
from thompson.context import Context
from thompson.bindings import Binding


def test_context_creation():
    b = Binding()
    c = Context(binding=b)
    assert c.binding == b
