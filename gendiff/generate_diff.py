import json
from gendiff.replace_bool import replace_bool
import pathlib
from pathlib import Path


def generate_diff(file1, file2):
    # путь до файлов
    dir_path = pathlib.Path.cwd()
    path1 = Path(dir_path, 'tests', 'fixtures', file1)
    path2 = Path(dir_path, 'tests', 'fixtures', file2)
    # открыть файлы формата json
    file_1 = json.load(open(path1))
    file_2 = json.load(open(path2))
    # замена булевых значений на строковые в словаре
    file_1 = replace_bool(file_1)
    file_2 = replace_bool(file_2)
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
