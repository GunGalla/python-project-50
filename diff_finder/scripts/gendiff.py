#!/usr/bin/env python3
"""Gendiff run script."""
from diff_finder.gendiff_argparse import parse_args
from diff_finder.generate_diff import generate_diff


def main():
    files = parse_args()
    print(generate_diff(files.first_file, files.second_file))


if __name__ == '__main__':
    main()
