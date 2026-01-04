from gendiff import generate_diff
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / 'test_data'

def read_file(file):
    return (DATA_DIR / file).read_text()

def test_gendiff_json():
    f1 = DATA_DIR / 'test_file1.json'
    f2 = DATA_DIR / 'test_file2.json'

    assert generate_diff(f1, f2) == read_file('test_result_file.txt')

def test_gendiff_yaml():
    f1 = DATA_DIR / 'test_file1.yaml'
    f2 = DATA_DIR / 'test_file2.yaml'

    assert generate_diff(f1, f2) == read_file('test_result_file.txt')

def test_gendiff_yaml1():
    f1 = DATA_DIR / 'test_rec_file1.yaml'
    f2 = DATA_DIR / 'test_rec_file2.yaml'

    assert generate_diff(f1, f2) == read_file('test_result_rec_file.txt')

def test_gendiff_json1():
    f1 = DATA_DIR / 'test_rec_file1.json'
    f2 = DATA_DIR / 'test_rec_file2.json'

    assert generate_diff(f1, f2) == read_file('test_result_rec_file.txt')

def test_gendiff_yaml_plain():
    f1 = DATA_DIR / 'test_rec_file1.yaml'
    f2 = DATA_DIR / 'test_rec_file2.yaml'

    assert generate_diff(f1, f2, 'plain') == read_file('test_result_plain.txt')

def test_gendiff_json_plain():
    f1 = DATA_DIR / 'test_rec_file1.json'
    f2 = DATA_DIR / 'test_rec_file2.json'

    assert generate_diff(f1, f2, 'plain') == read_file('test_result_plain.txt')

def test_gendiff_json_json():
    f1 = DATA_DIR / 'test_file1.json'
    f2 = DATA_DIR / 'test_file2.json'

    result = generate_diff(f1, f2, 'json')

    parsed = json.loads(result)

    assert isinstance(parsed, list) or isinstance(parsed, dict)