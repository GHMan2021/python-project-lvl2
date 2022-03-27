def replace_bool(source):
    for key, val in source.items():
        if type(val) == bool:
            source[key] = str(val).lower()
    return source
