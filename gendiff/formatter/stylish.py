"""Stylish format formatter"""
import itertools


def make_stylish(data):
    """Return stylish result"""

    result = stylish(data)

    return result


def stylish(items, depth=0):
    """Iterates data to create string in stylish format"""
    lines = []
    indent = '    ' * depth
    items.sort(key=lambda item: item['key'])
    for item in items:
        if item['action'] == 'old key':
            lines.append(build_line(item['key'], item['old_value'], '-', depth))

        elif item['action'] == 'new key':
            lines.append(build_line(item['key'], item['new_value'], '+', depth))

        elif item['action'] == 'no changes':
            lines.append(build_line(item['key'], item['old_value'], ' ', depth))

        elif item['action'] == 'new value':
            lines.append(build_line(item['key'], item['old value'], '-', depth))
            lines.append(build_line(item['key'], item['new value'], '+', depth))

        elif item['action'] == 'parent':
            lines.append(
                f"{indent}    {item['key']}: {stylish(item['child'], depth+1)}"
            )

    result = itertools.chain("{", lines, [indent + "}"])

    return '\n'.join(result)


def build_line(key, value, sign, depth):
    """Creates line from dict"""

    indent = ('    ' * depth)
    lines = []

    if isinstance(value, dict):
        lines.append(
            f'{indent}  {sign} {key}: {restruct_dict(value, depth+1)}'
        )

    else:
        lines.append(f'{indent}  {sign} {key}: {format_value(value)}')

    return '\n'.join(lines)


def restruct_dict(items, depth):
    """Restruct dict to string."""
    lines = []
    indent = '    ' * depth

    for key, value in sorted(items.items()):
        lines.append(build_line(key, value, ' ', depth))

    result = itertools.chain("{", lines, [indent + "}"])

    return '\n'.join(result)


def format_value(value):
    """Formatting string"""

    if isinstance(value, bool):
        formatted = str(value).lower()
    elif value is None:
        formatted = 'null'
    elif isinstance(value, (int, float)):
        formatted = str(value)
    elif value == '':
        formatted = ''
    else:
        formatted = f'{value}'
    return formatted
