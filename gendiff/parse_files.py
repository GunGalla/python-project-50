"""File detection and processing module."""
import json
import yaml


def open_file(filepath):
    """Check file format and load it."""
    with open(filepath, 'r') as f:
        return parse_file(f, filepath)


def parse_file(data, filepath):
    """Returns parsed files"""
    if filepath.endswith('.json'):
        return json.load(data)
    elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
        return yaml.safe_load(data)
    else:
        raise ValueError('Unsupported file format')
