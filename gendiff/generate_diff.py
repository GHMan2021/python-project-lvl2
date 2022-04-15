from .diff import diff
from .parser import parser
from .check_path_and_suffix import is_correct_file
from gendiff.formater import stylish, json_output, plain


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

    formater_dict = {
        'stylish': stylish,
        'plain': plain,
        'json': json_output
    }

    return formater_dict.get(format_name,
                             lambda x: 'Output format is undefined')(result)
