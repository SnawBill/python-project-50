from gendiff import generate_diff

from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / 'test_data'

def  read_file(file):
    return (DATA_DIR / file).read_text()

def test_gendiff_json():
    f1 = DATA_DIR / 'test_file1.json'
    f2 = DATA_DIR / 'test_file2.json'

    assert generate_diff(f1, f2) == read_file('test_result_file.txt')

def test_gendiff_yaml():
    f1 = DATA_DIR / 'test_file1.yaml'
    f2 = DATA_DIR / 'test_file2.yaml'

    assert generate_diff(f1, f2) == read_file('test_result_file.txt')

