import json
import yaml
from pathlib import Path
from gendiff.replace_bool import replace_bool


def generate_diff(file1, file2):
    path_file1 = Path(Path.cwd() / file1)
    path_file2 = Path(Path.cwd() / file2)
    path_files = [path_file1, path_file2]

    suffix_file1 = Path(Path(file1).name).suffix
    suffix_file2 = Path(Path(file2).name).suffix
    suffix_files = [suffix_file1, suffix_file2]

    list_files = []
    for i in range(2):
        if suffix_files[i] == '.json':
            file_json = json.load(open(path_files[i]))
            file_json = replace_bool(file_json)
            list_files.append(file_json)
        elif suffix_files[i] in ['.yml', '.yaml']:
            stream = open(path_files[i])
            file_yml = yaml.safe_load(stream)
            dict_files = {}
            for j in file_yml:
                dict_files.update(j)
            dict_files = replace_bool(dict_files)
            list_files.append(dict_files)
        else:
            return "File format is wrong"
    file_1 = list_files[0]
    file_2 = list_files[1]
    # сформировать уникальные значения в 2-х файлах, сортировка по алфавиту
    list_keys_1 = list(file_1.keys())
    list_keys_2 = list(file_2.keys())
    list_keys = set(list_keys_1 + list_keys_2)
    list_keys = sorted(list_keys)

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
