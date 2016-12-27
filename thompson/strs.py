# -*- coding: utf-8; -*-


def to_joined_strs(seq, sep=","):
    """
    >>> to_joined_strs((1, 2, 3,))
    '1,2,3'

    >>> to_joined_strs((1, 2, 3,), "| ")
    '1| 2| 3'

    >>> to_joined_strs((), "dhjleqhjeqhl")
    ''
    """
    return sep.join([str(i) for i in seq])
