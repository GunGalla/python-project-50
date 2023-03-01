"""Generate difference module"""
from gendiff.parse_files import parse_file, open_file
from gendiff.define_diff import define_difference
from gendiff.formatter.format import make_format


def generate_diff(file_path1, file_path2, format='stylish'):
    """Generates difference between two files"""
    data1 = parse_file(open_file(file_path1), file_path1)
    data2 = parse_file(open_file(file_path2), file_path2)
    diff = define_difference(data1, data2)
    result = make_format(diff, format)
    return result
