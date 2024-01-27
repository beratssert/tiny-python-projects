#!/usr/bin/env python3
"""Emulate wc (word count)"""

import argparse
import sys


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin],
                        help='Input file(s)')

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    inp = get_args().file

    total_lines_num, total_words_num, total_chars_num = 0, 0, 0
    for fh in inp:
        lines_num, words_num, chars_num = 0, 0, 0
        for line in fh:
            lines_num += 1
            words_num += len(line.split())
            chars_num += len(line)

        print(f'{lines_num:8}{words_num:8}{chars_num:8} {fh.name}')

        total_lines_num += lines_num
        total_words_num += words_num
        total_chars_num += chars_num

    if len(inp) > 1:
        print(
            f'{total_lines_num:8}{total_words_num:8}{total_chars_num:8} total')


if __name__ == '__main__':
    main()
