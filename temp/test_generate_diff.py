from gendiff import generate_diff


def test_generate_diff():
    diff = generate_diff(file1='file1.json', file2='file2.json')

    assert diff == \
           '{\n- follow: false\n  host: hexlet.io\n' \
           '- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true\n}'


def test_type_output():
    diff = generate_diff(file1='file1.json', file2='file2.json')

    assert isinstance(diff, str)
