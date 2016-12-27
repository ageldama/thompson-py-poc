# -*- coding: utf-8; -*-

from abc import abstractmethod
from thompson.nodes import Node


class LiteralNode(Node):
    def set(self, v):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        pass


class BoolVal(LiteralNode):
    def __init__(self, v):
        self.__v = v

    def set(self, v):
        # TODO: type-checking
        self.__v = v

    def get(self):
        return self.__v

    def __str__(self):
        return str(self.__v)


class NullVal(LiteralNode):
    def __str__(self):
        return "null"


class FunctionVal(LiteralNode):
    pass


class StringVal(LiteralNode):
    def __init__(self, v):
        self.__v = v

    def get(self):
        return self.__v

    def set(self, v):
        self.__v = v

    def __str__(self):
        return str(self.__v)
