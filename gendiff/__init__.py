from gendiff.diff import build_diff, result
from gendiff.parse import parse



def generate_diff(file_path1, file_path2):
    data1 = parse(file_path1)
    data2 = parse(file_path2)

    diff = build_diff(data1, data2)
    return result(diff)