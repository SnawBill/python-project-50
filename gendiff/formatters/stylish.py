def format_stylish(diff, depth=1):
    lines = []
    indent = ' ' * (depth * 4 - 2)

    for node in diff:
        key = node['key']
        node_type = node['type']

        if node_type == 'nested':
            children = format_stylish(node['children'], depth + 1)
            lines.append(
                f'{indent}  {key}: {{\n'
                f'{children}\n'
                f'{" " * (depth * 4)}}}'
            )

        elif node_type == 'unchanged':
            value = stringify(node['value'], depth + 1)
            lines.append(f'{indent}  {key}: {value}')

        elif node_type == 'added':
            value = stringify(node['value'], depth + 1)
            lines.append(f'{indent}+ {key}: {value}')

        elif node_type == 'removed':
            value = stringify(node['value'], depth + 1)
            lines.append(f'{indent}- {key}: {value}')

        elif node_type == 'changed':
            old = stringify(node['old_value'], depth + 1)
            new = stringify(node['new_value'], depth + 1)
            lines.append(f'{indent}- {key}: {old}')
            lines.append(f'{indent}+ {key}: {new}')

    return '\n'.join(lines)

def format_diff(diff):
    return '{\n' + format_stylish(diff) + '\n}'

def stringify(value, depth):
    if not isinstance(value, dict):
        if value is True:
            return 'true'
        if value is False:
            return 'false'
        if value is None:
            return 'null'
        return str(value)

    indent = ' ' * (depth * 4)
    lines = ['{']

    for key in sorted(value.keys()):
        val = value[key]
        lines.append(
            f'{indent}{key}: {stringify(val, depth + 1)}'
        )

    lines.append(' ' * ((depth - 1) * 4) + '}')
    return '\n'.join(lines)



