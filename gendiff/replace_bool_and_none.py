def replace_bool_and_none(val):
    if isinstance(val, bool):
        return str(val).lower()
    elif val is None:
        val = 'null'
        return val
    return val
