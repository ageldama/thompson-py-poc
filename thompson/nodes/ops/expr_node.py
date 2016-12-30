# -*- coding: utf-8; -*-
from thompson.nodes import Node
from abc import abstractmethod


class ExprNode(Node):
    @abstractmethod
    def __str__(self) -> str:
        pass


class NonExprNode(Node):
    @abstractmethod
    def __str__(self) -> str:
        pass
