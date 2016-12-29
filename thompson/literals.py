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

    @abstractmethod
    def __repr__(self):
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

    def __repr__(self):
        return "BoolVal({})".format(str(self.get()))

    def __str__(self):
        return str(self.get())


class NullVal(LiteralNode):
    def __eq__(self, other):
        return isinstance(other, NullVal)

    def __repr__(self):
        return "NullVal()"

    def __str__(self):
        return str(self.get())


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

    def __repr__(self):
        return "StringVal('{}')".format(self.get())

    def __str__(self):
        return str(self.get())


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

    def __repr__(self):
        return "NumberVal('{}')".format(self.get())

    def __str__(self):
        return str(self.get())


class FunctionVal(LiteralNode):
    def __init__(self, params, body, binding=NilConst):
        self.params = params
        self.body = body
        self.binding = binding

    def __repr__(self):
        return "FunctionVal({}, {}, {})".format(
            repr(self.binding), repr(self.params),
            repr(self.body))

    def __str__(self):
        return repr(self)  # FIXME: not-evalable-str.


class FunctionParamVal(LiteralNode):
    def __init__(self, name, **kwargs):
        self.name = name

    def __repr__(self):
        return "FunctionParamVal({})".format(repr(self.name))

    def __str__(self):
        return repr(self)
