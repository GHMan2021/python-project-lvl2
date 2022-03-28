from gendiff import generate_diff
from pathlib import Path


def test_generate_diff():
    file1 = Path(Path.cwd() / 'tests' / 'fixtures' / 'file1.json')
    file2 = Path(Path.cwd() / 'tests' / 'fixtures' / 'file2.json')
    diff = generate_diff(file1, file2)

    assert diff == \
           '{\n- follow: false\n  host: hexlet.io\n' \
           '- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true\n}'


def test_type_output():
    file1 = Path(Path.cwd() / 'tests' / 'fixtures' / 'file1.json')
    file2 = Path(Path.cwd() / 'tests' / 'fixtures' / 'file2.json')
    diff = generate_diff(file1, file2)

    assert isinstance(diff, str)
