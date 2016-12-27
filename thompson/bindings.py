# -*- coding: utf-8; -*-
"""Bindings.

Used to hold variables in expression-language. Also takes care of
binding-inheritances.
"""


class Binding(object):
    """Binding class.

    Each stackframe has own Binding, and Binding can has a parent.
    """
    def __init__(self, parent=None):
        """If `parent` parameter is absent, creates a root-binding."""
        self.parent = parent
        self.b = {}

    def contains(self, k):
        """Returns true/false, looking for `k` in whole inheritance-tree."""
        haz = self.contains_no_inherits(k)
        if haz:
            return haz
        elif self.parent is not None:
            return self.parent.contains(k)
        else:
            # it must be False.
            return haz

    def contains_no_inherits(self, k):
        """Returns true/false, but looking in this Binding, not on its
        parent."""
        return k in self.b

    def get(self, k):
        """Returns a value stored with `k` as a key,
        Looking on whole inheritance-tree.

        If its binding-tree doesn't have any matching key, it raises a
        `NameError` on that key.
        """
        if self.contains(k):
            cur = self
            while True:
                if cur.contains_no_inherits(k):
                    return cur.get_no_inherits(k)
                else:
                    cur = cur.parent
                    if cur is None:
                        raise Exception("what-the-fun")
        else:
            raise NameError(k)

    def get_no_inherits(self, k):
        """Look for `k` in this binding, without inheritance.

        No key is associated, raises `NameError` on `k`."""
        if k in self.b:
            return self.b[k]
        else:
            raise NameError(k)

    def set(self, k, v):
        """Simply sets a keyed value in this binding."""
        self.b[k] = v

    def set_uplevel(self, k, v):
        """Sets association in parent binding, if there's no parent, raises a
        `ValueError`.
        """
        if self.parent is None:
            raise ValueError("there is no parent for this binding!")
        else:
            self.parent.set(k, v)

    def set_global(self, k, v):
        """Sets association in root-binding. If there's no parent, then this
        is a root-binding."""
        cur = self
        while True:
            if cur.parent is None:
                break
            else:
                cur = cur.parent
        cur.set(k, v)
