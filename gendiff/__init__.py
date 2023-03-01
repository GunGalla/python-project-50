"""__init__.py for gendiff directory."""
from gendiff.generate_diff import generate_diff
from gendiff.gendiff_argparse import parse_args


__all__ = ('generate_diff', 'parse_args',)
