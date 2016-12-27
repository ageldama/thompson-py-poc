# -*- coding: utf-8; -*-

from abc import ABCMeta


class Node(metaclass=ABCMeta):
    pass


class BindingRef(Node):
    def __init__(self, k):
        self.k = k

    def __str__(self):
        return "BindingRef[{}]".format(self.k)
