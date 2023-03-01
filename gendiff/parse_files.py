"""File detection and processing module."""
import json
import yaml


def parse_file(filepath):
    """Check file format and load it."""
    with open(filepath, 'r') as file:
        if filepath.endswith('.json'):
            return json.load(file)
        elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
            return yaml.safe_load(file)
        else:
            raise ValueError('Unsupported file format')
