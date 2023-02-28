import pytest

from diff_finder.generate_diff import generate_diff


def test_with_empty_files():
    """Empty files test"""
    assert generate_diff("tests/fixtures/empty.json", "tests/fixtures/empty.json") == "{\n\n}"


def test_with_actual_files():
    """Filled files test"""
    with open('tests/fixtures/result_test.txt', 'r') as file:
        result = file.read()
    assert generate_diff("tests/fixtures/file1_test.json", "tests/fixtures/file2_test.json") == result
    assert generate_diff("tests/fixtures/file1_test.yml", "tests/fixtures/file2_test.yml") == result
    assert generate_diff("tests/fixtures/file1_test.json", "tests/fixtures/file2_test.yml") == result
