from gendiff.formatters.stylish import format_diff

def format(diff, format_name='stylish'):
    if format_name == 'stylish':
        return format_diff(diff)
    raise ValueError(f'Unknown format: {format_name}')