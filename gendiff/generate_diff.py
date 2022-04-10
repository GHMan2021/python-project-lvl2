import json
import yaml
from functools import wraps
from pathlib import Path
from gendiff.diff import diff
from gendiff.stylish import stylish


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
        file = open(file[0])
        file_json = json.load(file)
        file.close()
        return file_json
    stream = open(file[0])
    file_yml = yaml.safe_load(stream)
    return file_yml


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
    return stylish(result)
