import ply.yacc as yacc
from sexpr.lexer import tokens  # noqa: F401
from sexpr import Atom, Exprs


def p_toplevel(p):
    '''toplevel : atom
                | list'''
    p[0] = p[1]


def p_symbol(p):
    '''symbol : SYMBOL'''
    p[0] = Atom(p[1])
    lut = {Atom('true'): True,
           Atom('false'): False,
           Atom('nil'): None}
    if p[0] in lut:
        p[0] = lut[p[0]]


def p_atom(p):
    '''atom : symbol
            | STRING
            | NUMBER
            | list'''
    p[0] = p[1]


def p_exprs_1(p):
    '''exprs : atom'''
    exprs = Exprs()
    exprs.append(p[1])
    p[0] = exprs


def p_exprs_2(p):
    '''exprs : exprs atom'''
    exprs = p[1]
    exprs.append(p[2])
    p[0] = exprs


def p_list_0(p):
    '''list : LPAREN RPAREN'''
    p[0] = []


def p_list_1(p):
    '''list : LPAREN exprs RPAREN'''
    p[0] = [i for i in p[2]]


def p_error(t):
    print("Whoa. We're hosed")


parser = yacc.yacc(debug=False)


def parse_file(f):
    s = f.read()
    return parse(s)


def parse(s: str):
    return parser.parse(s)
