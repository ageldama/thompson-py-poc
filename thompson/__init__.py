# -*- coding: utf-8; -*-

from abc import ABCMeta, abstractmethod


class Node(metaclass=ABCMeta):
    pass


class ValueNode(Node):
    def set(self, v):
        raise NotImplementedError
    
    def get(self):
        raise NotImplementedError    
    
    @abstractmethod
    def __str__(self):
        pass


class BoolVal(ValueNode):
    def __init__(self, v):
        self.__v = v
        
    def set(self, v):
        # TODO: type-checking
        self.__v = v

    def get(self):
        return self.__v

    def __str__(self):
        return str(self.__v)


class NullVal(ValueNode):
    def __str__(self):
        return "null"


class FunctionVal(ValueNode):
    pass


class StringVal(ValueNode):
    pass


class ForeignVal(ValueNode):
    pass


class NumberVal(ValueNode):
    pass

