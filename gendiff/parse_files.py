"""File detection and processing module."""
import json
import yaml


def open_file(filepath):
    """Check file format and load it."""
    with open(filepath, 'r') as f:
        if filepath.endswith('.json'):
            file = json.load(f)
            return file
        else:
            file = f.read()
            return file


def parse_file(data, filepath):
    """Returns parsed files"""
    if filepath.endswith('.json'):
        return data
    elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
        return yaml.safe_load(data)
    else:
        raise ValueError('Unsupported file format')
