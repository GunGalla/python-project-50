"""Format definition module."""
from diff_finder.formatter.stylish import make_stylish
from diff_finder.formatter.plain import make_plain


def make_format(diff, format):
    """Apply format to data"""

    if format == 'stylish':
        return make_stylish(diff)
    elif format == 'plain':
        return make_plain(diff)
