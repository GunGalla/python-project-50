"""Test module for gendiff"""
import pytest
import os

from gendiff.generate_diff import generate_diff


def test_help():
    """Check gendiff help work"""
    assert os.system('gendiff -h') == 0


def test_with_empty_files():
    """Empty files test"""
    assert generate_diff("tests/fixtures/empty.json", "tests/fixtures/empty.json") == '{\n}'


def test_with_actual_flat_files():
    """Filled files test"""
    with open('tests/fixtures/result_test.txt', 'r') as file:
        result = file.read()
    assert generate_diff("tests/fixtures/file1_test.json", "tests/fixtures/file2_test.json") == result
    assert generate_diff("tests/fixtures/file1_test.yml", "tests/fixtures/file2_test.yml") == result
    assert generate_diff("tests/fixtures/file1_test.json", "tests/fixtures/file2_test.yml") == result


def test_nested_files_and_stylish_format():
    """Nested files diff test"""
    with open('tests/fixtures/result_nested.txt', 'r') as file:
        result = file.read()
    assert generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json") == result
    assert generate_diff("tests/fixtures/file1.yml", "tests/fixtures/file2.yml") == result
    assert generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.yml") == result


def test_plain_format():
    """Plain files diff test"""
    with open('tests/fixtures/result_plain.txt', 'r') as file:
        result = file.read()
    assert generate_diff(
        "tests/fixtures/file1.json", "tests/fixtures/file2.json", format='plain'
    ) == result
    assert generate_diff(
        "tests/fixtures/file1.yml", "tests/fixtures/file2.yml", format='plain'
    ) == result
    assert generate_diff(
        "tests/fixtures/file1.json", "tests/fixtures/file2.yml", format='plain'
    ) == result


def test_json_format():
    """Plain files diff test"""
    with open('tests/fixtures/result_json.txt', 'r') as file:
        result = file.read()
    assert generate_diff(
        "tests/fixtures/file1.json", "tests/fixtures/file2.json", format='json'
    ) == result
    assert generate_diff(
        "tests/fixtures/file1.yml", "tests/fixtures/file2.yml", format='json'
    ) == result
    assert generate_diff(
        "tests/fixtures/file1.json", "tests/fixtures/file2.yml", format='json'
    ) == result
