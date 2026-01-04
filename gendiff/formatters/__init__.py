from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_diff


def format(diff, format_name='stylish'):
    if format_name == 'stylish':
        return format_diff(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    raise ValueError(f'Unknown format: {format_name}')