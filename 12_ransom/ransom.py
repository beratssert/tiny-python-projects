#!/usr/bin/env python3
"""Ransom Note"""

import argparse
import random
import os


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input text or file')
    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        type=int,
                        default=None,
                        help='Random seed')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text, 'rt', encoding='utf-8').read().rstrip()

    return args


def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    print(''.join(map(choose, args.text)))


def choose(char):
    """Randomly choose an upper or lowercase letter to return"""

    return char.upper() if random.choice([0, 1]) else char.lower()


if __name__ == '__main__':
    main()
