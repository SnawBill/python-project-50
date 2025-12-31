def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff = []

    for key in keys:
        if key not in data1:
            diff.append(('added', key, data2[key]))
        elif key not in data2:
            diff.append(('removed', key, data1[key]))
        elif data1[key] != data2[key]:
            diff.append(('changed', key, data1[key], data2[key]))
        else:
            diff.append(('unchanged', key, data1[key]))
    
    return diff

def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value

def result(diff):
    result = ['{']
    for item in diff:

        status = item[0]

        if status == 'added':
            _, key, value = item
            result.append(f'  + {key}: {format_value(value)}')
        elif status == 'removed':
            _, key, value = item
            result.append(f'  - {key}: {format_value(value)}')
        elif status == 'unchanged':
            _, key, value = item
            result.append(f'    {key}: {format_value(value)}')
        elif status == 'changed':
            _, key, value1, value2 = item
            result.append(f'  - {key}: {format_value(value1)}')
            result.append(f'  + {key}: {format_value(value2)}')

    result.append('}')
    return '\n'.join(result)

