from .diff import diff
from .parser import parser
from .stylish import stylish
from .plain import plain
from .check_path_and_suffix import is_correct_file


def generate_diff(file1, file2, format_name=None):
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
    if format_name in ['stylish', None]:
        return stylish(result)
    elif format_name == 'plain':
        return plain(result)
    else:
        return 'Output format is undefined'
