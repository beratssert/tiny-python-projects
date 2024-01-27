#!/usr/bin/env python3
"""Gashlycrumb"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('letter',
                        metavar='letter',
                        type=str,
                        nargs='+',
                        help='Letter(s)')
    parser.add_argument('-f',
                        '--file',
                        metavar='FILE',
                        type=argparse.FileType('rt', encoding='utf-8'),
                        default='../inputs/gashlycrumb.txt',
                        help='Input file')

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()

    file = {line[0]: line.rstrip() for line in args.file}
    for letter in args.letter:
        print(file.get(letter.upper(), f'I do not know "{letter.upper()}".'))


if __name__ == '__main__':
    main()
