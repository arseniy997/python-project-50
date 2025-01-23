#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(prog='gendiff',
        description='Compares two configuration files and shows a difference.')

    # Add positional arguments
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    # Add -f / FORMAT
    parser.add_argument("-f", "--format", type=str,
        default='plain', help="set format of output")
    
    args = parser.parse_args()

    if args.help is True:
        parser.print_help()


if __name__ == '__main__':
    main()
