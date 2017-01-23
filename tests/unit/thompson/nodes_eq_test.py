# coding: utf-8
import thompson.evaluators.registry  # noqa: F401
from pytest import fixture
from thompson.nodes.literals import NilConst
from thompson.nodes.literals import BoolVal, NullVal
from thompson.nodes.literals import StringVal, NumberVal
from thompson.nodes.literals import FunctionVal
from thompson.nodes.literals import FunctionParamVal
from thompson.nodes.literals import MappedVal, MappedFunctionVal
from thompson.nodes.literals import NoWrappingMappedFunctionVal
from math import nan, inf
from thompson.nodes.ops import Prog1, ProgN, ParProg
from thompson.nodes.ops import LogNot, LogAnd, LogOr
from thompson.nodes.ops import ArithAdd, ArithSub
from thompson.nodes.ops import ArithMult, ArithMultMult
from thompson.nodes.ops import ArithDiv, ArithDivDiv, ArithRem
from thompson.nodes.ops import ComparLt, ComparLe
from thompson.nodes.ops import ComparGt, ComparGe
from thompson.nodes.ops import Equal, NotEqual
from thompson.nodes.ops import IsNull, IsNotNull
from thompson.nodes.ops import Assign, AssignUpvar, AssignGlobal, Const
from thompson.nodes.ops import BindingRef, Let
from thompson.nodes.ops import IfThenElse, When, Unless
from thompson.nodes.ops import CaseItem, CaseElse
from thompson.nodes.ops import CondItem, CondElse
from thompson.nodes.ops import Funcall, Pass


gen_a_alist = [
    ('str', lambda: StringVal('a')),
    ('nulls', lambda: NullVal()),
    ('bool-t', lambda: BoolVal(True)),
    ('bool-f', lambda: BoolVal(False)),
    ('num+42.1', lambda: NumberVal(42.1)),
    ('num+nan', lambda: NumberVal(nan)),
    ('num-nan', lambda: NumberVal(-nan)),
    ('num+inf', lambda: NumberVal(inf)),
    ('num-inf', lambda: NumberVal(-inf)),
    ('mapped-val', lambda: MappedVal('a')),
    ('mapped-fun-val',
     lambda: MappedFunctionVal('a', [FunctionParamVal('p')])),
    ('no-wrapping-mapped-fun-val',
     lambda: NoWrappingMappedFunctionVal('a', [FunctionParamVal('p')])),
    ('fun-param-val', lambda: FunctionParamVal('a')),
    ('prog1', lambda: Prog1([BoolVal(True), BoolVal(False)])),
    ('progn', lambda: ProgN([BoolVal(True), BoolVal(False)])),
    ('parprog', lambda: ParProg([BoolVal(True), BoolVal(False)])),
    ('log-not', lambda: LogNot(BoolVal(True))),
    ('log-and', lambda: LogAnd([BoolVal(True), BoolVal(False)])),
    ('log-or', lambda: LogOr([BoolVal(True), BoolVal(False)])),
    ('arith+', lambda: ArithAdd([NumberVal(1), NumberVal(2)])),
    ('arith-', lambda: ArithSub([NumberVal(1), NumberVal(2)])),
    ('arith*', lambda: ArithMult([NumberVal(1), NumberVal(2)])),
    ('arith**', lambda: ArithMultMult([NumberVal(1), NumberVal(2)])),
    ('arith/', lambda: ArithDiv([NumberVal(1), NumberVal(2)])),
    ('arith//', lambda: ArithDivDiv([NumberVal(1), NumberVal(2)])),
    ('arith-rem', lambda: ArithRem([NumberVal(1), NumberVal(2)])),
    ('compar-lt', lambda: ComparLt([NumberVal(1), NumberVal(2)])),
    ('compar-le', lambda: ComparLe([NumberVal(1), NumberVal(2)])),
    ('compar-gt', lambda: ComparGt([NumberVal(1), NumberVal(2)])),
    ('compar-ge', lambda: ComparGe([NumberVal(1), NumberVal(2)])),
    ('eq', lambda: Equal([NumberVal(1), NumberVal(2)])),
    ('ne', lambda: NotEqual([NumberVal(1), NumberVal(2)])),
    ('is-null', lambda: IsNull(NumberVal(2))),
    ('is-not-null', lambda: IsNotNull(NumberVal(2))),
    ('pass', lambda: Pass()),
    ('assign', lambda: Assign('k', NilConst)),
    ('assign-upvar', lambda: AssignUpvar('k', NilConst)),
    ('assign-global', lambda: AssignGlobal('k', NilConst)),
    ('binding-ref', lambda: BindingRef('k')),
    ('let', lambda: Let([Assign('k', NilConst),
                         Const('pi', 3.14),
                         AssignUpvar('u', NumberVal(42)),
                         AssignGlobal('g', BoolVal(True))],
                        ProgN([NilConst, Pass()]))),
    ('if-then-with-else',
     lambda: IfThenElse(Equal([StringVal('a'),
                               StringVal('a')]),
                        NumberVal(1), NumberVal(0))),
    ('if-then-without-else',
     lambda: IfThenElse(Equal([StringVal('a'),
                               StringVal('a')]),
                        NumberVal(1))),
    ('when', lambda: When(Equal([StringVal('a'), StringVal('a')]),
                          NumberVal(1))),
    ('unless', lambda: Unless(Equal([StringVal('a'), StringVal('a')]),
                              NumberVal(1))),
    ('case-item', lambda: CaseItem(StringVal('a'), NumberVal(42))),
    ('cond-item', lambda: CondItem(Equal([BindingRef('x'), StringVal('a')]),
                                   NumberVal(42))),
    ('case-with-else',
     lambda: CaseElse(NumberVal(42),
                      [CaseItem(NumberVal(42), StringVal('gotcha!')),
                       CaseItem(StringVal('42'), StringVal('gotcha-maybe'))],
                      StringVal('sorry'))),
    ('case-without-else',
     lambda: CaseElse(NumberVal(42),
                      [CaseItem(NumberVal(42), StringVal('gotcha!')),
                       CaseItem(StringVal('42'), StringVal('gotcha-maybe'))])),
    ('cond-with-else',
     lambda: CondElse([CondItem(Equal([BindingRef('x'), NumberVal(42)]),
                                StringVal('the answer!')),
                       CondItem(Equal([BindingRef('y'), BoolVal(False)]),
                                StringVal('no, not again!'))],
                      StringVal('fallback.'))),
    ('cond-without-else',
     lambda: CondElse([CondItem(Equal([BindingRef('x'), NumberVal(42)]),
                                StringVal('the answer!')),
                       CondItem(Equal([BindingRef('y'), BoolVal(False)]),
                                StringVal('no, not again!'))])),
    ('funcall', lambda: Funcall('f', [NumberVal(42), BoolVal(True)])),
    ('fun-val', lambda: FunctionVal(
        [FunctionParamVal('a'), FunctionParamVal('b')],
        ArithAdd([BindingRef('a'),
                  ArithSub([BindingRef('b'), 1])]))),
]


@fixture(params=[i[1] for i in gen_a_alist],
         ids=[i[0] for i in gen_a_alist])
def gen_a(request):
    return request.param


def test_eq(gen_a):
    a = gen_a()
    b = gen_a()
    assert a is not b
    assert a == b
