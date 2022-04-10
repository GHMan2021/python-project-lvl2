from gendiff.replace_bool import replace_bool


def diff(list_dicts):
    dict_1, dict_2 = list_dicts[0], list_dicts[1]
    list_keys_1, list_keys_2 = dict_1.keys(), dict_2.keys()

    result = []
    for key in sorted(list_keys_1 | list_keys_2):
        val_1 = replace_bool(dict_1.get(key))
        val_2 = replace_bool(dict_2.get(key))

        if all([isinstance(val_1, dict), isinstance(val_2, dict)]):
            result.append({'stat': 'DICT', 'key': key,
                           'children': diff([val_1, val_2])})

        else:
            if key not in list_keys_1:
                result.append({'stat': 'ADD', 'key': key, 'val': val_2})

            else:
                if key not in list_keys_2:
                    result.append({'stat': 'DEL', 'key': key, 'val': val_1})
                elif dict_1[key] == dict_2[key]:
                    result.append({'stat': 'EQUAL', 'key': key, 'val': val_1})

                else:
                    result.append({'stat': 'CHANGE', 'key': key,
                                   'val': {'DEL': val_1, 'ADD': val_2}})
    return result
