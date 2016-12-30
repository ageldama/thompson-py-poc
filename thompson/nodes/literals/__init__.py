# -*- coding: utf-8; -*-
from abc import abstractmethod
from thompson.nodes import Node
from typing import Union, Optional, Sequence, Any, Callable
from thompson.context import Binding
from thompson.nodes.ops.expr_node import ExprNode


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
    def __init__(self, v: bool):
        self.set(v)

    def set(self, v: bool):
        assert isinstance(v, bool)
        self.v = v

    def get(self) -> bool:
        return self.v

    def __eq__(self, other: 'BoolVal') -> bool:
        if not isinstance(other, BoolVal):
            raise TypeError()
        else:
            return self.get() == other.get()

    def __repr__(self) -> str:
        return "BoolVal({})".format(str(self.get()))

    def __str__(self) -> str:
        return str(self.get())


class NullVal(LiteralNode):
    def __eq__(self, other: 'NullVal') -> bool:
        return isinstance(other, NullVal)

    def __repr__(self) -> str:
        return "NullVal()"

    def __str__(self) -> str:
        return str(self.get())


NilConst = NullVal()


class StringVal(LiteralNode):
    def __init__(self, v: str):
        self.set(v)

    def get(self) -> str:
        return self.v

    def set(self, v: str) -> None:
        assert isinstance(v, str)
        self.v = v

    def __eq__(self, other: 'StringVal') -> bool:
        if not isinstance(other, StringVal):
            raise TypeError()
        else:
            return self.get() == other.get()

    def __repr__(self) -> str:
        return "StringVal('{}')".format(self.get())

    def __str__(self) -> str:
        return str(self.get())


class NumberVal(LiteralNode):
    def __init__(self, v: Union[int, float]):
        self.set(v)

    def get(self) -> Union[int, float]:
        return self.v

    def set(self, v: Union[int, float]):
        assert not isinstance(v, bool)
        assert isinstance(v, (int, float,))
        self.v = v

    def __eq__(self, other: 'NumberVal') -> bool:
        if not isinstance(other, NumberVal):
            raise TypeError()
        else:
            # TODO: epsilon comparison for floats?
            return self.get() == other.get()

    def __repr__(self) -> str:
        return "NumberVal('{}')".format(self.get())

    def __str__(self) -> str:
        return str(self.get())


class FunctionVal(LiteralNode):
    def __init__(self,
                 params: Sequence['FunctionParamVal'],
                 body: Union[LiteralNode, ExprNode],
                 binding: Optional[Binding]=NilConst):
        self.params = params
        self.body = body
        self.binding = binding

    def __repr__(self) -> str:
        return "FunctionVal({}, {}, {})".format(
            repr(self.binding), repr(self.params),
            repr(self.body))

    def __str__(self) -> str:
        return repr(self)  # FIXME: not-evalable-str.


class FunctionParamVal(LiteralNode):
    def __init__(self, name: str, **kwargs):
        self.name = name

    def __repr__(self) -> str:
        return "FunctionParamVal({})".format(repr(self.name))

    def __str__(self) -> str:
        return repr(self)


class MappedVal(LiteralNode):
    def __init__(self, v: Any):
        self.v = v

    def __repr__(self) -> str:
        return "MappedVal({})".format(repr(self.v))

    def __str__(self) -> str:
        return repr(self)


class MappedFunctionVal(LiteralNode):
    def __init__(self,
                 f: Callable,
                 params: Sequence['FunctionParamVal']):
        self.f = f
        self.params = params

    def __repr__(self) -> str:
        return "MappedFunctionVal({}, {})".format(
            repr(self.f), repr(self.params))

    def __str__(self) -> str:
        return repr(self)


class NoWrappingMappedFunctionVal(LiteralNode):
    def __init__(self,
                 f: Callable,
                 params: Sequence['FunctionParamVal']):
        self.f = f
        self.params = params

    def __repr__(self) -> str:
        return "NoWrappingMappedFunctionVal({}, {})".format(
            repr(self.f), repr(self.params))

    def __str__(self) -> str:
        return repr(self)
