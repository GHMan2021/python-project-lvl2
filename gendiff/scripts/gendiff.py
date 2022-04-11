#!/usr/bin/env python
import argparse
from gendiff import generate_diff
from gendiff.stylish import stylish


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', nargs='?', default='stylish',
                        help='output format (default: "stylish")')
    args = parser.parse_args()

    if args.format == 'stylish':
        print(stylish(generate_diff(args.first_file, args.second_file)))


if __name__ == '__main__':
    main()
