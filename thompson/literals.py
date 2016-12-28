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
        self.set(v)

    def set(self, v):
        assert isinstance(v, bool)
        self.v = v

    def get(self):
        return self.v

    def __eq__(self, other):
        if not isinstance(other, BoolVal):
            raise TypeError()
        else:
            return self.get() == other.get()

    def __str__(self):
        return str(self.v)


class NullVal(LiteralNode):
    def __eq__(self, other):
        return isinstance(other, NullVal)

    def __str__(self):
        return "nil"


NilConst = NullVal()


class StringVal(LiteralNode):
    def __init__(self, v):
        self.set(v)

    def get(self):
        return self.v

    def set(self, v):
        assert isinstance(v, str)
        self.v = v

    def __eq__(self, other):
        if not isinstance(other, StringVal):
            raise TypeError()
        else:
            return self.get() == other.get()

    def __str__(self):
        return str(self.v)


class NumberVal(LiteralNode):
    def __init__(self, v):
        self.set(v)

    def get(self):
        return self.v

    def set(self, v):
        assert not isinstance(v, bool)
        assert isinstance(v, (int, float,))
        self.v = v

    def __eq__(self, other):
        if not isinstance(other, NumberVal):
            raise TypeError()
        else:
            # TODO: epsilon comparison for floats?
            return self.get() == other.get()

    def __str__(self):
        return str(self.v)


class FunctionVal(LiteralNode):
    # TODO:
    pass
