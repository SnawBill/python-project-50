from gendiff.diff import build_diff
from gendiff.parse import parse
from gendiff.formatters import format



def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse(file_path1)
    data2 = parse(file_path2)

    diff = build_diff(data1, data2)
    return format(diff, format_name)