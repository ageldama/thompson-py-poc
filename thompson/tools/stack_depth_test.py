# -*- coding: utf-8; -*-
from thompson.nodes.literals import NumberVal
from thompson.nodes.ops import ArithAdd
from thompson.context import Context, Binding
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
