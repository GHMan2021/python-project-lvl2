from .diff import diff
from .parser import parser
from gendiff.formater.stylish import stylish
from gendiff.formater.plain import plain
from .check_path_and_suffix import is_correct_file
from gendiff.formater.json_output import json_output


def generate_diff(file1, file2, format_name='stylish'):
    list_dicts = []

    # проверка пути и формата файла, вывод соответствующего сообщения при ошибки
    for file in (file1, file2):
        if isinstance(is_correct_file(file), str):
            return is_correct_file(file)

        # функция подготовки содержимого файла в словарь
        dict_file = parser(file)
        list_dicts.append(dict_file)

    # вывод функции сравнения словарей
    result = diff(list_dicts)

    # вывод в соответствии с заданным форматом
    if format_name == 'stylish':
        return stylish(result)
    elif format_name == 'plain':
        return plain(result)
    elif format_name == 'json':
        return json_output(result)
    else:
        return 'Output format is undefined'
