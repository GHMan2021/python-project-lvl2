import json
import pytest
from gendiff import generate_diff


json1 = 'tests/fixtures/file1.json'
json2 = 'tests/fixtures/file2.json'
yml1 = 'tests/fixtures/filepath1.yml'
yml2 = 'tests/fixtures/filepath2.yml'


@pytest.fixture
def result_json_stylish():
    with open('tests/fixtures/result_diff', 'r') as f:
        return f.read()


@pytest.fixture
def result_json_plain():
    with open('tests/fixtures/result_diff_plain', 'r') as f:
        return f.read()


def test_generate_diff_returns_json_result(result_json_stylish):
    assert generate_diff(json1, json2, 'stylish') == result_json_stylish


def test_generate_diff_returns_yml_result(result_json_stylish):
    assert generate_diff(yml1, yml2) == result_json_stylish


def test_generate_diff_returns_yml_json_result(result_json_stylish):
    assert generate_diff(json1, yml2) == result_json_stylish


def test_generate_diff_returns_json_plain_result(result_json_plain):
    assert generate_diff(json1, json2, 'plain') == result_json_plain


def test_generate_diff_returns_err_format():
    assert generate_diff(json1, json2, 'foo') == 'Output format is undefined'


def test_generate_diff_returns_json_format_result():
    with open('tests/fixtures/result_diff_json.json') as f:
        result_json_format = json.load(f)

    assert generate_diff(json1, json2, 'json') == \
           json.dumps(result_json_format, indent=4)
