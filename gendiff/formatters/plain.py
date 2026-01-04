def walk(nodes, path, lines):
    for node in nodes:
        key = node['key']
        node_type = node['type']
        current_path = path + [key]
        property_name = '.'.join(current_path)

        if node_type == 'nested':
            walk(node['children'], current_path, lines)
        elif node_type == 'added':
            value = format_value(node['value'])
            lines.append(
                f"Property '{property_name}' was added with value: {value}"
                )
        elif node_type == 'removed':
            value = format_value(node['value'])
            lines.append(f"Property '{property_name}' was removed")
        elif node_type == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(
                f"Property '{property_name}' was updated. " 
                f"From {old_value} to {new_value}"
                )


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def format_plain(diff):
    lines = []
    walk(diff, [], lines)
    return '\n'.join(lines)