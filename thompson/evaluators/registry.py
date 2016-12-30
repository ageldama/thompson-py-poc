# -*- coding: utf-8; -*-
from thompson.nodes.ops import Pass, LogOr, LogAnd, LogNot
from thompson.nodes.ops import ArithAdd, ArithSub
from thompson.nodes.ops import ArithDiv, ArithDivDiv, ArithRem
from thompson.nodes.ops import ArithMult, ArithMultMult
from thompson.nodes.ops import ComparLt, ComparLe, ComparGt, ComparGe
from thompson.nodes.ops import Equal, NotEqual
from thompson.nodes.ops import IsNotNull, IsNull
from thompson.nodes.ops import BindingRef
from thompson.nodes.ops import Assign, AssignGlobal, AssignUpvar
from thompson.nodes.ops import Prog1, ProgN, ParProg
from thompson.nodes.ops import IfThenElse, When, Unless
from thompson.nodes.ops import CaseElse, CondElse
from thompson.nodes.ops import Funcall
from thompson.nodes.ops import Const, Let
from thompson.nodes.literals import LiteralNode
from thompson.nodes.literals import FunctionParamVal, FunctionVal
from thompson.nodes.literals import MappedVal, MappedFunctionVal
from thompson.nodes.literals import NoWrappingMappedFunctionVal
from thompson.evaluators.log_ops import LogNotEvaluator
from thompson.evaluators.log_ops import LogOrEvaluator
from thompson.evaluators.log_ops import LogAndEvaluator
from thompson.evaluators.arith_ops import ArithAddEvaluator, ArithSubEvaluator
from thompson.evaluators.arith_ops import ArithMultEvaluator
from thompson.evaluators.arith_ops import ArithMultMultEvaluator
from thompson.evaluators.arith_ops import ArithDivEvaluator
from thompson.evaluators.arith_ops import ArithDivDivEvaluator
from thompson.evaluators.arith_ops import ArithRemEvaluator
from thompson.evaluators.literals import LiteralEvaluator
from thompson.evaluators.compar_ops import ComparLtEvaluator, ComparLeEvaluator
from thompson.evaluators.compar_ops import ComparGtEvaluator, ComparGeEvaluator
from thompson.evaluators.assign import AssignEvaluator, AssignUpvarEvaluator
from thompson.evaluators.assign import AssignGlobalEvaluator, LetEvaluator
from thompson.evaluators.assign import BindingRefEvaluator, ConstEvaluator
from thompson.evaluators.sequentials import Prog1_Evaluator, ProgN_Evaluator
from thompson.evaluators.sequentials import ParProg_Evaluator
from thompson.evaluators.functionals import FunctionParamValEvaluator
from thompson.evaluators.functionals import FunctionValEvaluator
from thompson.evaluators.functionals import MappedValEvaluator
from thompson.evaluators.functionals import MappedFunctionValEvaluator
from thompson.evaluators.functionals import FuncallEvaluator
from thompson.evaluators.conditionals import IfThenElseEvaluator
from thompson.evaluators.conditionals import WhenEvaluator, UnlessEvaluator
from thompson.evaluators.conditionals import CaseElseEvaluator
from thompson.evaluators.conditionals import CondElseEvaluator
from thompson.evaluators.equals_and_nullity import EqualEvaluator
from thompson.evaluators.equals_and_nullity import NotEqualEvaluator
from thompson.evaluators.equals_and_nullity import IsNullEvaluator
from thompson.evaluators.equals_and_nullity import IsNotNullEvaluator
from thompson.evaluators.misc import PassEvaluator
from thompson.evaluators.utils import append_evaluator


# NOTE: `FunctionVal` should be before of `LiteralNode`.
# NOTE: (Due to it is a subtype of `LiteralNode`.)
append_evaluator(FunctionParamVal, FunctionParamValEvaluator())
append_evaluator(FunctionVal, FunctionValEvaluator())
append_evaluator(MappedVal, MappedValEvaluator())
append_evaluator(MappedFunctionVal, MappedFunctionValEvaluator())
append_evaluator(NoWrappingMappedFunctionVal, MappedFunctionValEvaluator())
append_evaluator(LiteralNode, LiteralEvaluator())
append_evaluator(LogOr, LogOrEvaluator())
append_evaluator(LogAnd, LogAndEvaluator())
append_evaluator(LogNot, LogNotEvaluator())
append_evaluator(ArithAdd, ArithAddEvaluator())
append_evaluator(ArithSub, ArithSubEvaluator())
append_evaluator(ArithMult, ArithMultEvaluator())
append_evaluator(ArithMultMult, ArithMultMultEvaluator())
append_evaluator(ArithRem, ArithRemEvaluator())
append_evaluator(ArithDiv, ArithDivEvaluator())
append_evaluator(ArithDivDiv, ArithDivDivEvaluator())
append_evaluator(ComparLt, ComparLtEvaluator())
append_evaluator(ComparLe, ComparLeEvaluator())
append_evaluator(ComparGe, ComparGeEvaluator())
append_evaluator(ComparGt, ComparGtEvaluator())
append_evaluator(Equal, EqualEvaluator())
append_evaluator(NotEqual, NotEqualEvaluator())
append_evaluator(IsNull, IsNullEvaluator())
append_evaluator(IsNotNull, IsNotNullEvaluator())
append_evaluator(Assign, AssignEvaluator())
append_evaluator(AssignUpvar, AssignUpvarEvaluator())
append_evaluator(AssignGlobal, AssignGlobalEvaluator())
append_evaluator(BindingRef, BindingRefEvaluator())
append_evaluator(Prog1, Prog1_Evaluator())
append_evaluator(ProgN, ProgN_Evaluator())
append_evaluator(ParProg, ParProg_Evaluator())
append_evaluator(IfThenElse, IfThenElseEvaluator())
append_evaluator(When, WhenEvaluator())
append_evaluator(Unless, UnlessEvaluator())
append_evaluator(CaseElse, CaseElseEvaluator())
append_evaluator(CondElse, CondElseEvaluator())
append_evaluator(Funcall, FuncallEvaluator())
append_evaluator(Pass, PassEvaluator())
append_evaluator(Const, ConstEvaluator())
append_evaluator(Let, LetEvaluator())
