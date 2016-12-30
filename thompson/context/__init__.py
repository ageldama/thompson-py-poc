# -*- coding: utf-8; -*-
from thompson.context.binding import Binding


class Context(object):
    def __init__(self, binding):
        self.binding = binding
