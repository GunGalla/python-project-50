"""Generate difference module"""
from diff_finder.parse_files import parse_file
from diff_finder.define_diff import define_difference
from diff_finder.formatter.format import make_format


def generate_diff(file_path1, file_path2, format='stylish'):
    """Generates difference between two files"""
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = define_difference(data1, data2)
    result = make_format(diff, format)
    return result
