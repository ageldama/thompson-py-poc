# -*- coding: utf-8; -*-


def eq_params(self, other, klass) -> bool:
    if not isinstance(other, klass):
        return False
    elif len(self.params) != len(other.params):
        return False
    else:
        return all([self.params[i] == other.params[i]
                    for i in range(len(self.params))])
