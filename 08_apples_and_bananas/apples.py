#!/usr/bin/env python3
"""Apples and bananas"""

import argparse
import os
import io


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input text or file')
    parser.add_argument('-v',
                        '--vowel',
                        metavar='vowel',
                        default='a',
                        choices=['a', 'e', 'i', 'o', 'u'],
                        help='The vowel to substitute')

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text, 'rt', encoding='utf-8')
    else:
        args.text = io.StringIO(args.text + '\n')

    return args


def main():
    """Make a jazz noise here"""

    args = get_args()

    changed_chars = []

    for line in args.text:
        for char in line:
            if char.lower() in 'aeiou':
                changed_chars.append(
                    args.vowel if char.islower() else args.vowel.upper())
            else:
                changed_chars.append(char)

    print(''.join(changed_chars), end='')


if __name__ == '__main__':
    main()
