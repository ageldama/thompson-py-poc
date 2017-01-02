# coding: utf-8
def enc_default(v, encoder):
    if v is None:
        return None
    else:
        return v.to_json_default(encoder)


def enc_defaults(vs, encoder):
    if vs is None:
        return None
    else:
        return [v.to_json_default(encoder) for v in vs]
