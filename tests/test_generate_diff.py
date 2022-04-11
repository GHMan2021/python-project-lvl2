from gendiff import generate_diff
from pathlib import Path


file1 = Path(Path.cwd() / 'tests/fixtures/file1.json')
file2 = Path(Path.cwd() / 'tests/fixtures/file2.json')
diff_json = generate_diff(file1, file2)

file11 = Path(Path.cwd() / 'tests/fixtures/filepath1.yml')
file22 = Path(Path.cwd() / 'tests/fixtures/filepath2.yml')
diff_yml = generate_diff(file11, file22)

diff_json_yml = generate_diff(file1, file22)


def test_generate_diff_returns_str():

    assert isinstance(diff_yml, str)
    assert isinstance(diff_json, str)
    assert isinstance(diff_json_yml, str)


def test_generate_diff_returns_json_result():
    result_json = open(Path(Path.cwd() / 'tests/fixtures/result_diff'))

    assert diff_json == result_json.read()


def test_generate_diff_returns_yml_result():
    result_yml = open(Path(Path.cwd() / 'tests/fixtures/result_diff'))

    assert diff_yml == result_yml.read()


def test_generate_diff_returns_yml_json_result():
    result_json_yml = open(Path(Path.cwd() / 'tests/fixtures/result_diff'))

    assert diff_json_yml == result_json_yml.read()


def test_generate_diff_returns_format_error():
    file1e = Path(Path.cwd() / 'tests/fixtures/file1.json')
    file2e = Path(Path.cwd() / 'tests/fixtures/result_diff')
    diff_json_e = generate_diff(file1e, file2e)

    assert diff_json_e == 'File format is wrong'


def test_generate_diff_returns_path_error():
    file1e = Path(Path.cwd() / 'tRsts/fixtures/file1.yml')
    file2e = Path(Path.cwd() / 'tests/fixtures/file2.yml')
    diff_yml_e = generate_diff(file1e, file2e)

    assert diff_yml_e == 'File path is wrong'
