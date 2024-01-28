#!/usr/bin/env python3
"""Telephone"""

import argparse
import random
import os
import string


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
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
    parser.add_argument('-m',
                        '--mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1,
                        help='Percent mutations')

    args = parser.parse_args()
    args.text = check_args(args, parser)

    return args


def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))

    text = args.text
    chars = list(text)

    number_of_mutation_chars = round(len(chars) * args.mutations)
    indexes = random.sample(range(len(chars)), number_of_mutation_chars)

    for i in indexes:
        chars[i] = random.choice(alpha.replace(chars[i], ''))

    changed_text = ''.join(chars)

    print(f'You said: "{text}"')
    print(f'I heard : "{changed_text}"')


def check_args(args, parser):
    """Checks if command-line arguments are valid and returns a text"""

    if args.mutations < 0 or args.mutations > 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        return open(args.text, 'rt', encoding='utf-8').read().rstrip()

    return args.text


if __name__ == '__main__':
    main()
