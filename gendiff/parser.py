import json
import yaml
from .check_path_and_suffix import path_and_suffix


@path_and_suffix
def parser(file):
    # file[0] - path
    # file[1] - suffix

    if file[1] == '.json':
        file = open(file[0])
        file_json = json.load(file)
        file.close()
        return file_json
    stream = open(file[0])
    file_yml = yaml.safe_load(stream)
    return file_yml
