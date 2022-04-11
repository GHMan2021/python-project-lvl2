from gendiff.parser import parser
from pathlib import Path


def test_parser_returns_result():
    file = Path(Path.cwd() / 'tests/fixtures/file1.json')
    result = parser(file)

    assert result == {
        'common': {
            'setting1': 'Value 1',
            'setting2': 200,
            'setting3': True,
            'setting6': {'key': 'value', 'doge': {'wow': ''}}},
        'group1': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}},
        'group2': {'abc': 12345, 'deep': {'id': 45}}
    }
