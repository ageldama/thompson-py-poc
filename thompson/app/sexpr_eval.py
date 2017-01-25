# -*- coding: utf-8; -*-
import sys
from pathlib import Path
import traceback
import thompson.evaluators.registry  # noqa
from thompson.sexprs.eval import evaluate_file, evaluate_str
from thompson.context import Context, Binding


def run(p):
    assert p.exists()
    c = Context(Binding())
    with p.open('r') as f:
        result = evaluate_file(f, c)
        return result


if __name__ == '__main__':
    if len(sys.argv) > 1:
        p = Path(sys.argv[1])
        print(run(p))
    else:
        print("""Thompson REL Implementation.
    * Jong-Hyouk Yun, Zalando SE, 2016.

Help:
    - Press Control-D or Enter `:q` to quit.
        """)
        c = Context(Binding())
        while True:
            try:
                s = input(';>> ')
                if s == ':q':
                    break
                result = evaluate_str(s, c)
                print(result)
            except EOFError as e:
                break
            except Exception as e:
                print(traceback.format_exc())
