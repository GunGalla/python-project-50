"""Generate difference module"""
from gendiff.parse_files import parse_file
from gendiff.define_diff import define_difference
from gendiff.formatter.format import make_format
import typing


def generate_diff(file_path1, file_path2, format='stylish'):
    """Generates difference between two files"""
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = define_difference(data1, data2)

    return make_format(diff, format)

if __name__ == '__main__':
    print(isinstance(generate_diff, typing.Callable))