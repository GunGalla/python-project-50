"""Generate difference module"""
import json


def generate_diff(file_path1, file_path2):
    """Generates difference between two files"""
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

    diff = {}

    for key in sorted(set(data1.keys()) | set(data2.keys())):
        if key not in data1:
            diff[f'  + {key}'] = str(data2[key]).lower()
        elif key not in data2:
            diff[f'  - {key}'] = str(data1[key]).lower()
        elif data1[key] != data2[key]:
            diff[f'  - {key}'] = str(data1[key]).lower()
            diff[f'  + {key}'] = str(data2[key]).lower()
        else:
            diff[f'    {key}'] = str(data1[key]).lower()
    result = '{\n'
    result += '\n'.join([f'{key}: {value}' for key, value in diff.items()])
    result += '\n}'
    print(result)
    return result
