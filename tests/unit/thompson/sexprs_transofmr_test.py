# -*- coding: utf-8; -*-
from pytest import fixture
from sexpr import Atom
from sexpr.parser import parse_file
from thompson.sexprs import to_st
from thompson.nodes.literals import NumberVal, BoolVal, StringVal, NilConst
from thompson.nodes.literals import FunctionVal, FunctionParamVal
from thompson.nodes.ops import BindingRef
from thompson.nodes.ops import Pass
from thompson.nodes.ops import LogAnd, LogOr, ArithAdd, ArithSub, ArithMult
from thompson.nodes.ops import ArithMultMult, ArithDivDiv, ArithRem, ArithDiv
from thompson.nodes.ops import ComparLt, ComparLe, ComparGt, ComparGe
from thompson.nodes.ops import Equal, NotEqual, Prog1, ProgN, ParProg
from thompson.nodes.ops import LogNot, IsNull, IsNotNull
from thompson.nodes.ops import Funcall, IfThenElse, When, Unless
from thompson.nodes.ops import Assign, AssignUpvar, AssignGlobal, Const
from thompson.nodes.ops import Let, CaseElse, CaseItem, CondElse, CondItem


def test_to_st_simple_atoms_and_literals():
    assert to_st(42) == NumberVal(42)
    assert to_st(Atom('true')) == BoolVal(True)
    assert to_st("foobar") == StringVal("foobar")
    assert to_st(Atom('nil')) == NilConst


def test_to_st_binding_ref_atoms():
    # any other non-reserved atoms as a binding-ref.
    assert to_st(Atom('foo')) == BindingRef('foo')
    assert to_st(Atom('foo?')) == BindingRef('foo?')
    assert to_st(Atom('+')) == BindingRef('+')


def test_list_as_non_form():
    # lists as a non-form.
    assert to_st([]) == []
    assert to_st([Atom('=')]) == []
    assert to_st([Atom('='), 1, 2]) == [NumberVal(1), NumberVal(2)]


def test_forms_without_param():
    assert to_st([Atom('pass')]) == Pass()


@fixture(params=[
    ([Atom('log-and'), Atom('true'), Atom('false')],
     LogAnd([BoolVal(True), BoolVal(False)])),
    ([Atom('log-or'), Atom('true'), Atom('false')],
     LogOr([BoolVal(True), BoolVal(False)])),
    ([Atom('+'), 1, 2],
     ArithAdd([NumberVal(1), NumberVal(2)])),
    ([Atom('+'), 1, 2, 3],
     ArithAdd([NumberVal(1), NumberVal(2), NumberVal(3)])),
    ([Atom('+')],
     ArithAdd([])),
    ([Atom('-'), 1, 2],
     ArithSub([NumberVal(1), NumberVal(2)])),
    ([Atom('*'), 1, 2],
     ArithMult([NumberVal(1), NumberVal(2)])),
    ([Atom('**'), 1, 2],
     ArithMultMult([NumberVal(1), NumberVal(2)])),
    ([Atom('/'), 1, 2],
     ArithDiv([NumberVal(1), NumberVal(2)])),
    ([Atom('//'), 1, 2],
     ArithDivDiv([NumberVal(1), NumberVal(2)])),
    ([Atom('rem'), 1, 2],
     ArithRem([NumberVal(1), NumberVal(2)])),
    ([Atom('<'), 1, 2],
     ComparLt([NumberVal(1), NumberVal(2)])),
    ([Atom('<='), 1, 2],
     ComparLe([NumberVal(1), NumberVal(2)])),
    ([Atom('>'), 1, 2],
     ComparGt([NumberVal(1), NumberVal(2)])),
    ([Atom('>='), 1, 2],
     ComparGe([NumberVal(1), NumberVal(2)])),
    ([Atom('eq?'), 1, 2],
     Equal([NumberVal(1), NumberVal(2)])),
    ([Atom('ne?'), 1, 2],
     NotEqual([NumberVal(1), NumberVal(2)])),
    ([Atom('prog1'), 1, 2],
     Prog1([NumberVal(1), NumberVal(2)])),
    ([Atom('progn'), 1, 2],
     ProgN([NumberVal(1), NumberVal(2)])),
    ([Atom('parprog'), 1, 2],
     ParProg([NumberVal(1), NumberVal(2)]))])
def forms_with_list_param(request):
    return request.param


def test_forms_with_list_param(forms_with_list_param):
    sexpr, st = forms_with_list_param
    assert to_st(sexpr) == st


@fixture(params=[([Atom('log-not'), Atom('true')],
                  LogNot(BoolVal(True))),
                 ([Atom('null?'), Atom('foo')],
                  IsNull(BindingRef('foo'))),
                 ([Atom('not-null?'), Atom('foo')],
                  IsNotNull(BindingRef('foo'))),
                 ([Atom('set'), 'foo', Atom('bar')],
                  Assign(StringVal('foo'), BindingRef('bar'))),
                 ([Atom('set^'), 'foo', Atom('bar')],
                  AssignUpvar(StringVal('foo'), BindingRef('bar'))),
                 ([Atom('set/'), 'foo', Atom('bar')],
                  AssignGlobal(StringVal('foo'), BindingRef('bar'))),
                 ([Atom('const'), 'foo', Atom('bar')],
                  Const(StringVal('foo'), BindingRef('bar'))),
                 ([Atom('fncall'), Atom('inc'), [Atom('='), Atom('bar')]],
                  Funcall(BindingRef('inc'), [BindingRef('bar')])),
                 ([Atom('if'), [Atom('eq?'), Atom('x'), 42], [Atom('pass')]],
                  IfThenElse(Equal([BindingRef('x'), NumberVal(42)]),
                             Pass())),
                 ([Atom('if'), [Atom('eq?'), Atom('x'), 42],
                   [Atom('pass')], [Atom('set'), 'foo', 'bar']],
                  IfThenElse(Equal([BindingRef('x'), NumberVal(42)]),
                             Pass(),
                             Assign(StringVal('foo'), StringVal('bar')))),
                 ([Atom('when'), [Atom('eq?'), Atom('x'), 42],
                   [Atom('pass')]],
                  When(Equal([BindingRef('x'), NumberVal(42)]), Pass())),
                 ([Atom('unless'), [Atom('eq?'), Atom('x'), 42],
                   [Atom('pass')]],
                  Unless(Equal([BindingRef('x'), NumberVal(42)]),
                         Pass()))])
def forms_with_applying_params(request):
    return request.param


def test_form_with_applying_params(forms_with_applying_params):
    sexpr, st = forms_with_applying_params
    assert to_st(sexpr) == st


def test_special_forms():
    assert to_st([Atom('fn'), [Atom('x'), Atom('y')],
                  [Atom('+'), Atom('x'), Atom('y')]]) == \
                  FunctionVal([FunctionParamVal('x'), FunctionParamVal('y')],
                              ArithAdd([BindingRef('x'), BindingRef('y')]))
    assert to_st([Atom('let'), [], [Atom('pass')]]) == \
        Let([], Pass())
    # let + {const, assign}
    let_sexpr = [Atom('let'), [[Atom('const'), 'pi', 3.14],
                               [Atom('set'), 'x', 42]], [Atom('pass')]]
    let_st = Let([Const(StringVal('pi'), NumberVal(3.14)),
                  Assign(StringVal('x'), NumberVal(42))], Pass())
    assert to_st(let_sexpr) == let_st
    # case-with-else.
    case1_sexpr = [Atom('case'), Atom('x'),
                   [[42, 'the answer!'],
                    [3.14, 'pi']],
                   Atom('false')]
    case1_st = CaseElse(BindingRef('x'),
                        [CaseItem(NumberVal(42), StringVal('the answer!')),
                         CaseItem(NumberVal(3.14), StringVal('pi'))],
                        BoolVal(False))
    assert to_st(case1_sexpr) == case1_st
    # case-without-else.
    case2_sexpr = [Atom('case'), Atom('x'),
                   [[42, 'the answer!'],
                    [3.14, 'pi']]]
    case2_st = CaseElse(BindingRef('x'),
                        [CaseItem(NumberVal(42), StringVal('the answer!')),
                         CaseItem(NumberVal(3.14), StringVal('pi'))])
    assert to_st(case2_sexpr) == case2_st
    # cond-without-else.
    cond1_sexpr = [Atom('cond'),
                   [[[Atom('>'), Atom('x'), 18], 'too old'],
                    [[Atom('<='), Atom('x'), 18], 'too young']]]
    cond1_st = CondElse([CondItem(ComparGt([BindingRef('x'), NumberVal(18)]),
                                  StringVal('too old')),
                         CondItem(ComparLe([BindingRef('x'), NumberVal(18)]),
                                  StringVal('too young'))])
    assert to_st(cond1_sexpr) == cond1_st
    # cond-with-else.
    cond2_sexpr = [Atom('cond'),
                   [[[Atom('>'), Atom('x'), 18], 'too old'],
                    [[Atom('<='), Atom('x'), 18], 'too young']],
                   'immortal']
    cond2_st = CondElse([CondItem(ComparGt([BindingRef('x'), NumberVal(18)]),
                                  StringVal('too old')),
                         CondItem(ComparLe([BindingRef('x'), NumberVal(18)]),
                                  StringVal('too young'))],
                        StringVal('immortal'))
    assert to_st(cond2_sexpr) == cond2_st


def test_syntactic_sugar_fncall_form():
    assert to_st([Atom('awesome-fun'), 42, 'foo']) == \
        Funcall(BindingRef('awesome-fun'), [NumberVal(42), StringVal('foo')])


def test_compose_fn_sexpr(test_data_path):
    fn = test_data_path / 'closure_compose.sexpr'
    with fn.open('r') as f:
        result = parse_file(f)
    st = to_st(result)
    expect = Let(
        [Assign(StringVal('inc1'), FunctionVal([FunctionParamVal('x')],
                                               ArithAdd([NumberVal(1),
                                                         BindingRef('x')]))),
         Assign(StringVal('sq'), FunctionVal([FunctionParamVal('x')],
                                             ArithMult([BindingRef('x'),
                                                        BindingRef('x')]))),
         Assign(StringVal('compose'), FunctionVal([FunctionParamVal('g'),
                                                   FunctionParamVal('f')],
                                                  FunctionVal([FunctionParamVal('x')],  # noqa: E501
                                                              Funcall(BindingRef('g'),  # noqa: E501
                                                                      [Funcall(BindingRef('f'), [BindingRef('x')])]))))],  # noqa: E501
        Funcall(BindingRef('g.f'), [NumberVal(2)]))
    assert st == expect
