# -*- coding: utf-8; -*-
from abc import abstractmethod
import math
from thompson.nodes import Evaluatable
from typing import Union, Optional, Sequence, Any, Callable
from thompson.context import Binding
from thompson.jsons import enc_defaults, enc_default


class LiteralNode(Evaluatable):
    def set(self, v):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError

    @abstractmethod
    def __eq__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class BoolVal(LiteralNode):
    def __init__(self, v: bool) -> None:
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
        return self.__repr__()

    def to_json_default(self, json_encoder):
        return {'bool': self.get()}


# TODO: singleton?
class NullVal(LiteralNode):
    def __init__(self, *arg) -> None:
        pass

    def get(self):
        return None

    def __eq__(self, other: 'NullVal') -> bool:
        return isinstance(other, NullVal)

    def __repr__(self) -> str:
        return "NullVal()"

    def __str__(self) -> str:
        return self.__repr__()

    def to_json_default(self, json_encoder):
        return {'null': None}


NilConst = NullVal()


class StringVal(LiteralNode):
    def __init__(self, v: str) -> None:
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
        return self.__repr__()

    def to_json_default(self, json_encoder):
        return {'str': self.get()}


class NumberVal(LiteralNode):
    def __init__(self, v: Union[int, float]) -> None:
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
        elif math.isinf(self.get()) and math.isinf(other.get()):
            return True
        elif math.isnan(self.get()) and math.isnan(other.get()):
            return True
        else:
            # TODO: epsilon comparison for floats?
            return self.get() == other.get()

    def __repr__(self) -> str:
        return "NumberVal('{}')".format(self.get())

    def __str__(self) -> str:
        return self.__repr__()

    def to_json_default(self, json_encoder):
        return {'num': self.get()}


class FunctionVal(LiteralNode):
    def __init__(self,
                 params: Sequence['FunctionParamVal'],
                 body: Evaluatable,
                 binding: Optional[Binding]=NilConst) -> None:
        self.params = params
        self.body = body
        self.binding = binding

    def __eq__(self, other) -> bool:
        if not isinstance(other, FunctionVal):
            return False
        else:
            # NOTE: only compares literal values, not its binding.
            return self.params == other.params \
                and self.body == other.body

    def __repr__(self) -> str:
        return "FunctionVal({}, {}, {})".format(
            repr(self.binding), repr(self.params),
            repr(self.body))

    def __str__(self) -> str:
        return repr(self)  # FIXME: not-evalable-str.

    def to_json_default(self, json_encoder):
        # NOTE: exclude binding.
        return {'fun': {'params': enc_defaults(self.params, json_encoder),
                        'body': enc_default(self.body, json_encoder)}}


class FunctionParamVal(LiteralNode):
    def __init__(self, name: str, **kwargs) -> None:
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, FunctionParamVal):
            return False
        else:
            return self.name == other.name

    def __repr__(self) -> str:
        return "FunctionParamVal({})".format(repr(self.name))

    def __str__(self) -> str:
        return repr(self)

    def to_json_default(self, json_encoder):
        return {'fun-param': self.name}


class MappedVal(LiteralNode):
    def __init__(self, v: Any) -> None:
        self.v = v

    def __eq__(self, other):
        if not isinstance(other, MappedVal):
            return False
        else:
            return self.v == other.v

    def __repr__(self) -> str:
        return "MappedVal({})".format(repr(self.v))

    def __str__(self) -> str:
        return repr(self)

    def to_json_default(self, json_encoder):
        raise ValueError('MappedVal is cannot be serialized!')


class MappedFunctionVal(LiteralNode):
    def __init__(self,
                 f: Callable,
                 params: Sequence['FunctionParamVal']) -> None:
        self.f = f
        self.params = params

    def __eq__(self, other):
        if not isinstance(other, MappedFunctionVal):
            return False
        else:
            return self.f is other.f \
                and self.params == other.params

    def __repr__(self) -> str:
        return "MappedFunctionVal({}, {})".format(
            repr(self.f), repr(self.params))

    def __str__(self) -> str:
        return repr(self)

    def to_json_default(self, json_encoder):
        raise ValueError('MappedFunctionVal is cannot be serialized!')


class NoWrappingMappedFunctionVal(LiteralNode):
    def __init__(self,
                 f: Callable,
                 params: Sequence['FunctionParamVal']) -> None:
        self.f = f
        self.params = params

    def __eq__(self, other):
        if not isinstance(other, NoWrappingMappedFunctionVal):
            return False
        else:
            return self.f == other.f \
                and self.params == other.params

    def __repr__(self) -> str:
        return "NoWrappingMappedFunctionVal({}, {})".format(
            repr(self.f), repr(self.params))

    def __str__(self) -> str:
        return repr(self)

    def to_json_default(self, json_encoder):
        raise ValueError(
            'NoWrappingMappedFunctionVal is cannot be serialized!')
