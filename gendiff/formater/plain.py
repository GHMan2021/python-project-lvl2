import itertools
from gendiff.replace_bool_and_none import replace_bool_and_none


def check_dict_val(value):
    if isinstance(value, dict):
        result = '[complex value]'
    elif any([type(value) == bool, value is None]):
        result = replace_bool_and_none(value)
    elif type(value) == str:
        result = f"'{value}'"
    else:
        result = value
    return result


def not_stat_dict(_dict):
    if _dict['stat'] == 'DEL':
        line = f"Property '{_dict['key']}' was removed"

    elif _dict['stat'] == 'ADD':
        _dict['val'] = check_dict_val(_dict['val'])
        line = f"Property '{_dict['key']}' was added with value: {_dict['val']}"

    else:
        _dict['val']['DEL'] = check_dict_val(_dict['val']['DEL'])
        _dict['val']['ADD'] = check_dict_val(_dict['val']['ADD'])

        line = f"Property '{_dict['key']}' was updated. " \
               f"From {_dict['val']['DEL']} to {_dict['val']['ADD']}"

    return line


def plain(lists):
    prn = []
    for _dict in lists:
        if _dict['stat'] == 'DICT':

            for _d in _dict['children']:
                _d['key'] = f"{_dict['key']}.{_d['key']}"

            res = plain(_dict['children'])
            prn.append(res)

        elif _dict['stat'] == "EQUAL":
            continue

        else:
            prn.append(not_stat_dict(_dict))

    result = itertools.chain(prn)
    return '\n'.join(result)
