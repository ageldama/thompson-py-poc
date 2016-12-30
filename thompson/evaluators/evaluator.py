# -*- coding: utf-8; -*-
from abc import abstractmethod


class Evaluator(object):
    @abstractmethod
    def eval(self, context, node):
        pass
