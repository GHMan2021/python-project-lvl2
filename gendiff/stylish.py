import itertools
from .diff import diff
from .replace_bool_and_none import replace_bool_and_none


def stylish(value):

    def iter_(_dicts, depth):
        prn = []

        for current_value in _dicts:

            cv_v = current_value.get('val', None)
            cv_ch = current_value.get('children', None)
            cv_k = current_value['key']
            cv_s = current_value['stat']
            indent_size = depth * ' '

            if cv_s == 'ADD':
                if isinstance(cv_v, dict):
                    res = iter_((diff([cv_v, cv_v])), depth + 4)
                    prn.append(f"{indent_size}+ {cv_k}: {res}")
                else:
                    prn.append(
                        f"{indent_size}+ {cv_k}: {replace_bool_and_none(cv_v)}")

            elif cv_s == 'DEL':
                if isinstance(cv_v, dict):
                    res = iter_((diff([cv_v, cv_v])), depth + 4)
                    prn.append(f"{indent_size}- {cv_k}: {res}")
                else:
                    prn.append(
                        f"{indent_size}- {cv_k}: {replace_bool_and_none(cv_v)}")

            elif cv_s == 'EQUAL':
                prn.append(
                    f"{indent_size}  {cv_k}: {replace_bool_and_none(cv_v)}")

            elif cv_s == 'CHANGE':
                if isinstance(cv_v['DEL'], dict):
                    res = iter_((diff([cv_v['DEL'], cv_v['DEL']])), depth + 4)
                    prn.append(f"{indent_size}- {cv_k}: {res}")
                else:
                    prn.append(f"{indent_size}- {cv_k}: "
                               f"{replace_bool_and_none(cv_v['DEL'])}")

                if isinstance(cv_v['ADD'], dict):
                    res = iter_((diff([cv_v['ADD'], cv_v['ADD']])), depth + 4)
                    prn.append(f"{indent_size}+ {cv_k}: {res}")
                else:
                    prn.append(f"{indent_size}+ {cv_k}: "
                               f"{replace_bool_and_none(cv_v['ADD'])}")

            else:
                prn.append(f"{indent_size}  {cv_k}: "
                           f"{iter_(cv_ch, depth + 4)}")

        result = itertools.chain("{", prn, [(depth - 2) * ' ' + "}"])
        return '\n'.join(result)

    return iter_(value, 2)
