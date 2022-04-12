import json
from gendiff import generate_diff
from pathlib import Path


file1 = Path(Path.cwd() / 'tests/fixtures/file1.json')
file2 = Path(Path.cwd() / 'tests/fixtures/file2.json')
diff_json = generate_diff(file1, file2, 'stylish')
diff_json_plain = generate_diff(file1, file2, 'plain')

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


def test_generate_diff_returns_json_plain_result():
    result_json = open(Path(Path.cwd() / 'tests/fixtures/result_diff_plain'))

    assert diff_json_plain == result_json.read()


def test_generate_diff_returns_yml_result():
    result_yml = open(Path(Path.cwd() / 'tests/fixtures/result_diff'))

    assert diff_yml == result_yml.read()


def test_generate_diff_returns_yml_json_result():
    result_json_yml = open(Path(Path.cwd() / 'tests/fixtures/result_diff'))

    assert diff_json_yml == result_json_yml.read()


def test_generate_diff_returns_err_format():
    diff_json_err = generate_diff(file1, file2, 'foo')

    assert diff_json_err == 'Output format is undefined'


def test_generate_diff_returns_json_format_result():
    diff_json_format = generate_diff(file1, file2, 'json')

    file = open(Path(Path.cwd() / 'tests/fixtures/result_diff_json.json'))
    result_json_format = json.load(file)

    assert diff_json_format == json.dumps(result_json_format, indent=4)
