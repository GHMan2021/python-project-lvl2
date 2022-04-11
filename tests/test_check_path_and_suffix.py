from gendiff import generate_diff
from pathlib import Path


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
