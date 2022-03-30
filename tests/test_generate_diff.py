import sys
sys.path.append(r"/home/yuri/python-project-lvl2/gendiff")
from gendiff.generate_diff import generate_diff
from pathlib import Path


def test_generate_diff():
    file1 = Path(Path.cwd() / 'tests' / 'fixtures' / 'file1.json')
    file2 = Path(Path.cwd() / 'tests' / 'fixtures' / 'file2.json')
    diff = generate_diff(file1, file2)
    result_json = open(Path(Path.cwd() / 'tests' / 'fixtures' / 'result_json'))

    assert diff == result_json.read()


def test_type_output():
    file1 = Path(Path.cwd() / 'tests' / 'fixtures' / 'file1.json')
    file2 = Path(Path.cwd() / 'tests' / 'fixtures' / 'file2.json')
    diff = generate_diff(file1, file2)

    assert isinstance(diff, str)
