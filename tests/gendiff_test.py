import json

import pytest

from diff_finder.gendiff import generate_diff

@pytest.fixture
def result():
    """Fixture for tests"""
    return '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

def test_with_empty_files():
    """Empty files test"""
    assert generate_diff("tests/fixtures/empty.json", "tests/fixtures/empty.json") == "{\n\n}"


def test_with_actual_files(result):
    """Filled files test"""
    assert generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json") == result
