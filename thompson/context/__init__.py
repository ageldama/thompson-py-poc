# -*- coding: utf-8; -*-
from thompson.context.binding import Binding  # noqa: F401


class Context(object):
    def __init__(self, binding):
        self.binding = binding
