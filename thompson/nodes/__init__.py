# -*- coding: utf-8; -*-

from abc import ABCMeta, abstractmethod


class Node(metaclass=ABCMeta):
    @abstractmethod
    def to_json_default(self, json_encoder):
        pass


class Evaluatable(Node):
    pass
