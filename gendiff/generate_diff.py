import json
import yaml
from functools import wraps
from pathlib import Path
from gendiff.replace_bool import replace_bool


def path_and_suffix(func):
    @wraps(func)
    def wrapper(file):
        path_file = Path(Path.cwd() / file)
        suffix_file = Path(Path(file).name).suffix
        data_file_tuple = (path_file, suffix_file)
        return func(data_file_tuple)
    return wrapper


@path_and_suffix
def is_correct_file(file):
    if not file[0].exists():
        return "File path is wrong"

    if file[1] not in ['.json', '.yml', '.yaml']:
        return "File format is wrong"


@path_and_suffix
def prepare_dict(file):
    if file[1] == '.json':
        file_json = json.load(open(file[0]))
        file_json = replace_bool(file_json)
        return file_json
    stream = open(file[0])
    file_yml = yaml.safe_load(stream)
    dict_files = {}
    for j in file_yml:
        dict_files.update(j)
    dict_files = replace_bool(dict_files)
    return dict_files


def diff(list_dicts):
    file_1, file_2 = list_dicts[0], list_dicts[1]
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
    return result


def output(result):
    prn = "{\n"
    for i in result:
        prn += i + '\n'
    prn = prn + '}'
    return prn


def generate_diff(file1, file2):
    list_dicts = []

    # проверка пути и формата файла, вывод соответствующего сообщения при ошибки
    for file in (file1, file2):
        if isinstance(is_correct_file(file), str):
            return is_correct_file(file)
        # функция подготовки содержимого файла в словарь
        dict_file = prepare_dict(file)
        list_dicts.append(dict_file)

    # функция сравнения словарей
    result = diff(list_dicts)

    # функция вывода результата в заданном формате
    return output(result)
