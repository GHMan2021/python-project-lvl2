from functools import wraps
from pathlib import Path


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
