# -*- coding: utf-8; -*-
from typing import io
from thompson.json_encdec import loads as json_loads
from thompson.context import Context
from thompson.evaluators import evaluate
import thompson.evaluators.registry  # noqa
# I'm sorry, above one-line is a magic.


def evaluate_json_str(c: Context, s: str) -> 'Node':
    return evaluate(c, json_loads(s))


def evaluate_json_file(c: Context, f: io) -> 'Node':
    return evaluate_json_str(c, f.read())
