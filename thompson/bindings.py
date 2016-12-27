# -*- coding: utf-8; -*-


class Binding(object):
    def __init__(self, parent=None):
        self.parent = parent
        self.b = {}

    def contains(self, k):
        haz = self.contains_no_inherits(k)
        if haz:
            return haz
        elif self.parent is not None:
            return self.parent.contains(k)
        else:
            # it must be False.
            return haz

    def contains_no_inherits(self, k):
        return k in self.b

    def get(self, k):
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
        if k in self.b:
            return self.b[k]
        else:
            raise NameError(k)

    def set(self, k, v):
        self.b[k] = v

    def set_uplevel(self, k, v):
        if self.parent is None:
            raise ValueError("there is no parent for this binding!")
        else:
            self.parent.set(k, v)

    def set_global(self, k, v):
        cur = self
        while True:
            if cur.parent is None:
                break
            else:
                cur = cur.parent
        #
        cur.set(k, v)
