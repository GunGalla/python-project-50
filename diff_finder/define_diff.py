"""Module to define difference between two files."""


def define_difference(items1, items2):
    """Finds files difference."""

    keys = sorted(set(items1.keys()) | set(items2.keys()))
    result = []
    for key in keys:
        diff_result = {'key': key}

        if key not in items2.keys():
            diff_result['action'] = 'old key'
            diff_result['old_value'] = items1[key]

        elif key not in items1.keys():
            diff_result['action'] = 'new key'
            diff_result['new_value'] = items2[key]

        elif items1[key] == items2[key]:
            diff_result['action'] = 'no changes'
            diff_result['old_value'] = items1[key]

        elif isinstance(items1[key], dict) and isinstance(items2[key], dict):
            diff_result['action'] = 'parent'
            diff_result['child'] = define_difference(items1[key], items2[key])

        else:
            diff_result['action'] = 'new value'
            diff_result['old value'] = items1[key]
            diff_result['new value'] = items2[key]
        result.append(diff_result)
    return result
