"""Plain format formatter."""


def make_plain(data):
    """Return plain result"""

    result = plain(data)

    return result


def plain(items, path=''):
    """Iterates data to create string in plain format"""
    lines = []
    items.sort(key=lambda item: item['key'])

    for item in items:
        if path:
            absolute_path = f"{path}.{item['key']}"

        else:
            absolute_path = item['key']

        if item['action'] == 'old_key':
            lines.append(f"Property '{absolute_path}' was removed")

        elif item['action'] == 'new_key':
            lines.append(
                f"Property '{absolute_path}' was added "
                f"with value: {format_value(item['new_value'])}")

        elif item['action'] == 'new_value':
            lines.append(
                f"Property '{absolute_path}' was updated. "
                f"From {format_value(item['old_value'])} "
                f"to {format_value(item['new_value'])}")

        elif item['action'] == 'parent':
            lines.append(plain(item['child'], absolute_path))

    '\n'.join(lines)

    return '\n'.join(lines)


def format_value(value):
    """Formatting string"""

    if isinstance(value, bool):
        formatted = str(value).lower()
    elif value is None:
        formatted = 'null'
    elif isinstance(value, (int, float)):
        formatted = str(value)
    elif isinstance(value, dict):
        formatted = '[complex value]'
    else:
        formatted = f"'{value}'"
    return formatted
