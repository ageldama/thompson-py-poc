# -*- coding: utf-8; -*-
from thompson.literals import NumberVal
from thompson.builtin_operators import ArithAdd
from thompson.context import Context
from thompson.bindings import Binding
from thompson.evaluators import evaluate


def main():
    c = Context(Binding())

    def E(expr):
        evaluate(c, expr)

    N = NumberVal
    count = 0
    BASE = ArithAdd(N(1), N(1))
    cur = BASE
    while True:
        try:
            E(cur)
            count = count + 1
            cur = ArithAdd(N(1), cur)
        except:
            break
    print("max = ", count)


if __name__ == '__main__':
    main()
