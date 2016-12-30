# -*- coding: utf-8; -*-
from typing import Sequence


def to_joined_strs(seq: Sequence, sep: str=",") -> str:
    """
    >>> to_joined_strs((1, 2, 3,))
    '1,2,3'

    >>> to_joined_strs((1, 2, 3,), "| ")
    '1| 2| 3'

    >>> to_joined_strs((), "dhjleqhjeqhl")
    ''
    """
    return sep.join([str(i) for i in seq])
