import json
import yaml
from pathlib import Path
from gendiff.replace_bool import replace_bool


def get_list_files(file1, file2):
    suffix_files = list(map(lambda x: Path(Path(x).name).suffix,(file1, file2)))

    path_files = list(map(lambda x: Path(Path.cwd() / x), (file1, file2)))

    list_files = []
    i = 0
    for _ in suffix_files:
        if _ not in ['.json', 'yml', 'yaml']:
            return "File format is wrong"

        if _ == '.json':
            file_json = json.load(open(path_files[i]))
            file_json = replace_bool(file_json)
            list_files.append(file_json)
            i = 1
        else:
            stream = open(path_files[i])
            file_yml = yaml.safe_load(stream)
            dict_files = {}
            for j in file_yml:
                dict_files.update(j)
            dict_files = replace_bool(dict_files)
            list_files.append(dict_files)
            i = 1
    return list_files


def generate_diff(file1, file2):
    list_files = get_list_files(file1, file2)

    file_1, file_2 = list_files[0], list_files[1]
    list_keys_1, list_keys_2 = list(file_1.keys()), list(file_2.keys())

    list_keys = sorted(set(list_keys_1 + list_keys_2))

    result = []
    for key in list_keys:
        if key not in list_keys_1:
            line = ("+ " + str(key) + ": " + str(file_2[key]))
            result.append(line)
        else:
            if key not in list_keys_2:
                line = ("- " + str(key) + ": " + str(file_1[key]))
                result.append(line)
            elif file_1[key] == file_2[key]:
                line = ("  " + str(key) + ": " + str(file_1[key]))
                result.append(line)
            else:
                line_1 = ("- " + str(key) + ": " + str(file_1[key]))
                line_2 = ("+ " + str(key) + ": " + str(file_2[key]))
                result.append(line_1)
                result.append(line_2)
    prn = "{\n"
    for i in result:
        prn += i + '\n'
    prn = prn + '}'
    return prn
