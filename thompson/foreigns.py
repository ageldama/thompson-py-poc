# -*- coding: utf-8; -*-
from thompson.nodes import Node


# TODO: should be a LiteralNode?
class ForeignValueNode(Node):
    pass


class ForeignVal(ForeignValueNode):
    pass


class ForeignFunc(ForeignValueNode):
    pass


class NumberVal(ForeignValueNode):
    pass
