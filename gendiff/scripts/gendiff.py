#!/usr/bin/env python3
"""Gendiff run script."""
from gendiff.gendiff_argparse import parse_args
from gendiff.generate_diff import generate_diff


def main():
    """Starts diff script"""
    files = parse_args()
    diff = generate_diff(files.first_file, files.second_file, files.format)
    print(diff)


if __name__ == '__main__':
    main()
