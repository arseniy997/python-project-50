#!/usr/bin/env python3
import json


def generate_diff(file_path1, file_path2):

    # Convert json files to dictionaries
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))

    # Make a sorted set of all keys in both docs
    list_of_keys = list(file1.keys()) + list(file2.keys())
    set_of_keys = sorted(set(list_of_keys))

    # Check difference
    diff = []
    for key in set_of_keys:
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                diff_line = f'  {key}: {file1[key]}'
            else:
                diff_line = f'- {key}: {file1[key]}\n  + {key}: {file2[key]}'
        elif key in file1:
            diff_line = f'- {key}: {file1[key]}'
        elif key in file2:
            diff_line = f'+ {key}: {file2[key]}'

        diff.append('  ' + diff_line)

    result = '\n'.join(diff)
    return "{\n" + result + "\n}"


# if __name__ == '__main__':
#     print('Cannot run this module. Run a script instead.')

print(generate_diff('/home/myubuntu/python-project-50/file1.json', 
    '/home/myubuntu/python-project-50/file2.json'))
