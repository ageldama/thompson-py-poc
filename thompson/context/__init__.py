# -*- coding: utf-8; -*-
from thompson.context.binding import Binding


class Context(object):
    def __init__(self, binding: Binding) -> None:
        self.binding = binding  # type: Binding
