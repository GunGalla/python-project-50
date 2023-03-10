"""Format definition module."""
from gendiff.formatter.stylish import make_stylish
from gendiff.formatter.plain import make_plain
from gendiff.formatter.json import make_json


def make_format(diff, format):
    """Apply format to data"""

    if format == 'stylish':
        return make_stylish(diff)
    elif format == 'plain':
        return make_plain(diff)
    elif format == 'json':
        return make_json(diff)
