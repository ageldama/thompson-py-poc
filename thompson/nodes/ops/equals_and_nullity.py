# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode


class Equal(ExprNode):
    def __init__(self,
                 a: 'Evaluatable',
                 b: 'Evaluatable'):
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "Equal[{}, {}]".format(str(self.a), str(self.b))


class NotEqual(ExprNode):
    def __init__(self,
                 a: 'Evaluatable',
                 b: 'Evaluatable'):
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "NotEqual[{}, {}]".format(str(self.a), str(self.b))


class IsNull(ExprNode):
    def __init__(self, a: 'Evaluatable'):
        self.a = a

    def __str__(self) -> str:
        return "IsNull[{}]".format(str(self.a))


class IsNotNull(ExprNode):
    def __init__(self, a: 'Evaluatable'):
        self.a = a

    def __str__(self) -> str:
        return "IsNotNull[{}]".format(str(self.a))
