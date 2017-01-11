# -*- coding: utf-8; -*-
import sys
import thompson.evaluators.registry  # noqa
from thompson.json_eval import evaluate_json_file
from thompson.context import Context, Binding
from pathlib import Path


if __name__ == '__main__':
    if len(sys.argv) > 1:
        p = Path(sys.argv[1])
        assert p.exists()
        c = Context(Binding)
        with p.open('r') as f:
            result = evaluate_json_file(c, f)
            print(result)
    else:
        print("Please pass .json filename as an argument.")
