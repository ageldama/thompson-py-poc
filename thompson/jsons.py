# coding: utf-8
def enc_default(v, encoder):
    if v is None:
        return None
    elif isinstance(v, (str, int, float, bool,)):
        return v
    else:
        return v.to_json_default(encoder)


def enc_defaults(vs, encoder):
    if vs is None:
        return []
    else:
        return [v.to_json_default(encoder) for v in vs]
