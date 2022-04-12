from gendiff.formater.plain import check_dict_val
import json


def json_output(lists):
    res = {
        "ADD": [],
        "CHANGE": [],
        "DEL": []
    }

    def iter_(_dicts):

        for current_value in _dicts:

            cv_v = current_value.get('val', None)
            cv_ch = current_value.get('children', None)
            cv_k = current_value['key']
            cv_s = current_value['stat']

            if cv_s == 'ADD':
                res.get("ADD").append({cv_k: check_dict_val(cv_v)})

            elif cv_s == 'DEL':
                res.get("DEL").append({cv_k: check_dict_val(cv_v)})

            elif cv_s == 'CHANGE':
                res.get("CHANGE").append({cv_k: check_dict_val(cv_v['ADD'])})

            elif cv_s == 'EQUAL':
                continue

            else:
                for _d in cv_ch:
                    _d['key'] = f"{cv_k}.{_d['key']}"
                iter_(cv_ch)

        return json.dumps(res, indent=4)

    return iter_(lists)
