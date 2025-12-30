import argparse

import json


def parse(path_to_file):
    with open(path_to_file) as file:
        return json.load(file)

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    data1 = parse(args.first_file)
    data2 = parse(args.second_file)

if __name__ == '__main__':
    main()