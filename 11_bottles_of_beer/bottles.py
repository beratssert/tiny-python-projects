#!/usr/bin/env python3
"""Bottles of beer song"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n',
                        '--num',
                        metavar='number',
                        type=int,
                        default=10,
                        help='How many bottles')
    args = parser.parse_args()

    if args.num < 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


def main():
    """Make a jazz noise here"""

    args = get_args()
    print('\n\n'.join(map(verse, range(args.num, 0, -1))))


def verse(bottles):
    """Get a sing"""

    bottle_str = 'bottles' if bottles > 1 else 'bottle'
    last_bottle = bottles - 1
    last_bottle_str = f'{last_bottle} bottles' if last_bottle > 1 else '1 bottle' if last_bottle == 1 else 'No more bottles'

    return '\n'.join([
        f'{bottles} {bottle_str} of beer on the wall,',
        f'{bottles} {bottle_str} of beer,', 'Take one down, pass it around,',
        f'{last_bottle_str} of beer on the wall!'
    ])


def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])


if __name__ == '__main__':
    main()
