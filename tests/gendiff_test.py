"""Test module for gendiff"""
import os
import pytest

from gendiff.generate_diff import generate_diff


def test_help():
    """Check gendiff help work"""
    assert os.system('gendiff -h') == 0


def test_with_empty_files():
    """Empty files test"""
    assert generate_diff("tests/fixtures/empty.json", "tests/fixtures/empty.json") == '{\n}'


@pytest.mark.parametrize(
    "file_1, file_2",
    [("tests/fixtures/file1_test.json", "tests/fixtures/file2_test.json"),
     ("tests/fixtures/file1_test.yml", "tests/fixtures/file2_test.yml"),
     ("tests/fixtures/file1_test.json", "tests/fixtures/file2_test.yml"),
     ],
)
def test_with_actual_flat_files(file_1, file_2):
    """Filled files test"""
    with open('tests/fixtures/result_test.txt', 'r') as file:
        result = file.read()
    assert generate_diff(file_1, file_2) == result


@pytest.mark.parametrize(
    "file_1, file_2",
    [("tests/fixtures/file1.json", "tests/fixtures/file2.json"),
     ("tests/fixtures/file1.yml", "tests/fixtures/file2.yml"),
     ("tests/fixtures/file1.json", "tests/fixtures/file2.yml"),
     ],
)
def test_nested_files_and_stylish_format(file_1, file_2):
    """Nested files diff test"""
    with open('tests/fixtures/result_nested.txt', 'r') as file:
        result = file.read()
    assert generate_diff(file_1, file_2) == result


@pytest.mark.parametrize(
    "file_1, file_2, format",
    [("tests/fixtures/file1.json", "tests/fixtures/file2.json", "plain"),
     ("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", "plain"),
     ("tests/fixtures/file1.json", "tests/fixtures/file2.yml", "plain"),
     ],
)
def test_plain_format(file_1, file_2, format):
    """Plain files diff test"""
    with open('tests/fixtures/result_plain.txt', 'r') as file:
        result = file.read()
    assert generate_diff(file_1, file_2, format) == result


@pytest.mark.parametrize(
    "file_1, file_2, format",
    [("tests/fixtures/file1.json", "tests/fixtures/file2.json", "json"),
     ("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", "json"),
     ("tests/fixtures/file1.json", "tests/fixtures/file2.yml", "json"),
     ],
)
def test_json_format(file_1, file_2, format):
    """Plain files diff test"""
    with open('tests/fixtures/result_json.txt', 'r') as file:
        result = file.read()
    assert generate_diff(file_1, file_2, format) == result
