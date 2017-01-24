# -*- coding: utf-8; -*-
from sexpr import Atom
from thompson.nodes.literals import StringVal, BoolVal, NumberVal
from thompson.nodes.literals import NilConst
from thompson.nodes.ops import Ref
from thompson.nodes.ops import Pass
from thompson.nodes.ops import LogAnd, LogOr, ArithAdd, ArithSub
from thompson.nodes.ops import ArithMult, ArithMultMult
from thompson.nodes.ops import ArithDiv, ArithDivDiv, ArithRem
from thompson.nodes.ops import ComparLt, ComparLe, ComparGt, ComparGe
from thompson.nodes.ops import Equal, NotEqual
from thompson.nodes.ops import LogNot, IsNull, IsNotNull
from thompson.nodes.ops import Assign, AssignUpvar, AssignGlobal
from thompson.nodes.ops import Const, Funcall
from thompson.nodes.ops import When, Unless, IfThenElse
from thompson.nodes.ops import Prog1, ProgN, ParProg


__to_st = {
    'fn': None,  # SPECIAL
    'let': None,  # SPECIAL
    'case': None,  # SPECIAL
    'cond': None,  # SPECIAL
}

_to_st_no = {
    'pass': Pass,
}

_to_st_list_params = {
    'log-and': LogAnd,
    'log-or': LogOr,
    '+': ArithAdd,
    '-': ArithSub,
    '*': ArithMult,
    '**': ArithMultMult,
    '/': ArithDiv,
    '//': ArithDivDiv,
    'rem': ArithRem,
    '<': ComparLt,
    '<=': ComparLe,
    '>': ComparGt,
    '>=': ComparGe,
    'eq?': Equal,
    'ne?': NotEqual,
    'prog1': Prog1,
    'progn': ProgN,
    'parprog': ParProg,
}

_to_st_apply_params = {
    'log-not': (LogNot, ['a']),
    'null?': (IsNull, ['a']),
    'not-null?': (IsNotNull, ['a']),
    'set': (Assign, ['dst', 'src']),
    'set^': (AssignUpvar, ['dst', 'src']),
    'set/': (AssignGlobal, ['dst', 'src']),
    'const': (Const, ['dst', 'src']),
    'fncall': (Funcall, ['fun', 'params']),
    'if': (IfThenElse, ['cond', 'then_clause', 'else_clause']),
    'when': (When, ['cond', 'then_clause']),
    'unless': (Unless, ['cond', 'then_clause']),
}


def to_st(sexpr):
    """Transform a S-expression into Syntax-Tree."""
    if isinstance(sexpr, str):
        return StringVal(sexpr)
    elif isinstance(sexpr, (int, float,)):
        return NumberVal(sexpr)
    elif isinstance(sexpr, Atom):
        if sexpr.val == 'nil':
            return NilConst
        elif sexpr.val == 'true':
            return BoolVal(True)
        elif sexpr.val == 'false':
            return BoolVal(False)
        else:
            # anything else is just a refs.
            return Ref(sexpr.val)
    elif isinstance(sexpr, list):
        if len(sexpr) == 0:
            return sexpr
        elif isinstance(sexpr[0], Atom):
            k = sexpr[0].val
            if k in _to_st_no.keys():
                return _to_st_no[k]()
            elif k in _to_st_list_params.keys():
                return _to_st_list_params[k]([to_st(i) for i in sexpr[1:]])
            elif k in _to_st_apply_params.keys():
                pass  # TODO:
            else:
                raise ValueError("Form {} not matched!".format(sexpr))
        else:
            # TODO: ???
            raise ValueError("Wrong form of a list! ({})".format(sexpr))
    else:
        raise ValueError("What the {} is?".format(sexpr))


def from_st(st):
    """Transform a Syntax-Tree into S-expression."""
    pass
