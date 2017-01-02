# -*- coding: utf-8; -*-
from thompson.nodes import Node, Evaluatable
from abc import abstractmethod


class ExprNode(Evaluatable):
    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __eq__(self, other) -> bool:
        pass


class NonExprNode(Node):
    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __eq__(self, other) -> bool:
        pass
