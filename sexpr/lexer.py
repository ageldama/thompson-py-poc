# -*- coding: utf-8; -*-
import ply.lex as lex


tokens = (
    'NUMBER',
    'STRING',
    'SYMBOL',
    'LPAREN',
    'RPAREN',
    'LSQBRACKET',
    'RSQBRACKET',
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSQBRACKET = r'\['
t_RSQBRACKET = r'\]'
t_SYMBOL = r'([A-Z]|[a-z]|[0-9]|\!|\$|\%|\&|\*|\+|\-|\.|\/|\:|\<|\=|\>|\?|\@|\^|\_|\~)+'  # noqa: E501
t_ignore_COMMENT = r'\;.*'


def t_NUMBER(t):
    r'\-?\d+(\.\d+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t


def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    #r'\".*\"'
    t.value = str(t.value[1:-1])
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def produce_tokens(data):
    result = []
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        result.append(tok)
    return result


lexer = lex.lex()
