# -*- coding: utf-8; -*-
from thompson.nodes.ops.expr_node import ExprNode


class ComparLt(ExprNode):
    def __init__(self, a: 'Evaluatable', b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "ComparLt[{}, {}]".format(str(self.a), str(self.b))


class ComparLe(ExprNode):
    def __init__(self, a: 'Evaluatable', b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "ComparLe[{}, {}]".format(str(self.a), str(self.b))


class ComparGt(ExprNode):
    def __init__(self, a: 'Evaluatable', b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "ComparGt[{}, {}]".format(str(self.a), str(self.b))


class ComparGe(ExprNode):
    def __init__(self, a: 'Evaluatable', b: 'Evaluatable') -> None:
        self.a, self.b = a, b

    def __str__(self) -> str:
        return "ComparGe[{}, {}]".format(str(self.a), str(self.b))
