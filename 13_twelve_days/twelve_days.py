#!/usr/bin/env python3
"""Twelve Days of Christmas"""

import argparse
import sys


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n',
                        '--num',
                        metavar='days',
                        type=int,
                        default=12,
                        help='Number of days to sing')
    parser.add_argument('-o',
                        '--outfile',
                        metavar='file',
                        type=argparse.FileType('wt'),
                        default=sys.stdout,
                        help='Outfile')

    args = parser.parse_args()

    if args.num < 1 or args.num > 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


def main():
    """Make a jazz noise here"""

    args = get_args()
    verses = map(verse, range(1, args.num + 1))
    args.outfile.write('\n\n'.join(verses) + '\n')


def verse(num):
    """Sing a verse"""

    ordinal = {
        1: 'first',
        2: 'second',
        3: 'third',
        4: 'fourth',
        5: 'fifth',
        6: 'sixth',
        7: 'seventh',
        8: 'eighth',
        9: 'ninth',
        10: 'tenth',
        11: 'eleventh',
        12: 'twelfth',
    }

    gifts = [
        'A partridge in a pear tree.', 'Two turtle doves,',
        'Three French hens,', 'Four calling birds,', 'Five gold rings,',
        'Six geese a laying,', 'Seven swans a swimming,',
        'Eight maids a milking,', 'Nine ladies dancing,',
        'Ten lords a leaping,', 'Eleven pipers piping,',
        'Twelve drummers drumming,'
    ]

    sing = [
        f'On the {ordinal.get(num)} day of Christmas,',
        'My true love gave to me,'
    ]

    sing += reversed(gifts[:num])

    if num != 1:
        sing[-1] = 'And a partridge in a pear tree.'

    return '\n'.join(sing)


def test_verse():
    """Test verse"""

    assert verse(1) == '\n'.join([
        'On the first day of Christmas,', 'My true love gave to me,',
        'A partridge in a pear tree.'
    ])

    assert verse(2) == '\n'.join([
        'On the second day of Christmas,', 'My true love gave to me,',
        'Two turtle doves,', 'And a partridge in a pear tree.'
    ])


if __name__ == '__main__':
    main()
