"""Module to describe how gendiff works."""
import argparse


def description():
    """Command line description."""
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.parse_args()
