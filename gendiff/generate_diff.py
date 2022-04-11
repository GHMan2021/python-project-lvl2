from gendiff.diff import diff
from gendiff.parser import is_correct_file, parser


def generate_diff(file1, file2):
    list_dicts = []

    # проверка пути и формата файла, вывод соответствующего сообщения при ошибки
    for file in (file1, file2):
        if isinstance(is_correct_file(file), str):
            return is_correct_file(file)
        # функция подготовки содержимого файла в словарь
        dict_file = parser(file)
        list_dicts.append(dict_file)

    # вывод функции сравнения словарей
    return diff(list_dicts)
