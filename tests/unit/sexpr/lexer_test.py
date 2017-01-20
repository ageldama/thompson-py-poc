# -*- coding: utf-8; -*-
from sexpr.lexer import produce_tokens


WHATEVER = object()


def match_tok(tok, expect_type, expect_val):
    if tok is None:
        return False
    elif tok.type != expect_type:
        return False
    elif expect_val is WHATEVER:
        return True
    else:
        return tok.value == expect_val


def test_string():
    assert match_tok(produce_tokens('"foo bar"')[0], "STRING", "foo bar")
    assert match_tok(produce_tokens('""')[0], "STRING", "")


def test_boolean():
    assert match_tok(produce_tokens('"true"')[0], "STRING", "true")
    assert match_tok(produce_tokens('true')[0], "SYMBOL", 'true')
    assert match_tok(produce_tokens('false')[0], "SYMBOL", 'false')


def test_nil():
    assert match_tok(produce_tokens('nil')[0], "SYMBOL", 'nil')


def test_symbol():
    toks = produce_tokens('foo bar zoo + - +1')
    assert match_tok(toks[0], "SYMBOL", "foo")
    assert match_tok(toks[1], "SYMBOL", "bar")
    assert match_tok(toks[2], "SYMBOL", "zoo")
    assert match_tok(toks[3], "SYMBOL", "+")
    assert match_tok(toks[4], "SYMBOL", "-")
    assert match_tok(toks[5], "SYMBOL", "+1")


def test_number():
    toks = produce_tokens('42 -42 0 1.23 -3.14')
    assert match_tok(toks[0], "NUMBER", 42)
    assert match_tok(toks[1], "NUMBER", -42)
    assert match_tok(toks[2], "NUMBER", 0)
    assert match_tok(toks[3], "NUMBER", 1.23)
    assert match_tok(toks[4], "NUMBER", -3.14)


def test_parens_comment():
    toks = produce_tokens("""
      (+ 123 "foo bar" true nil ;; comment?)
         )
    """)
    assert match_tok(toks[0], "LPAREN", WHATEVER)
    assert match_tok(toks[1], "SYMBOL", "+")
    assert match_tok(toks[2], "NUMBER", 123)
    assert match_tok(toks[3], "STRING", "foo bar")
    assert match_tok(toks[4], "SYMBOL", 'true')
    assert match_tok(toks[5], "SYMBOL", 'nil')
    assert match_tok(toks[6], "RPAREN", WHATEVER)
