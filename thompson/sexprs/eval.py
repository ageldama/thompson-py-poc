# -*- coding: utf-8; -*-
from thompson.context import Context, Binding
from thompson.evaluators import evaluate
from sexpr.parser import parse_file, parse
from thompson.sexprs import to_st


def evaluate_file(f, context=Context(Binding())):
    sexpr = parse_file(f)
    st = to_st(sexpr)
    result = evaluate(context, st)
    return result


def evaluate_str(s, context=Context(Binding())):
    sexpr = parse(s)
    st = to_st(sexpr)
    result = evaluate(context, st)
    return result
