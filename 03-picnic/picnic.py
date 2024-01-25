#!/usr/bin/env python3
"""Picnic game"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(description='Picnic game')
    parser.add_argument('str', help='Item(s) to bring', nargs='+')
    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    food = args.str if not args.sorted else sorted(args.str)

    bringing = ""
    if len(food) == 1:
        bringing = food[0]
    elif len(food) == 2:
        bringing = ' and '.join(food)
    elif len(food) > 2:
        food[-1] = 'and ' + food[-1]
        bringing = ', '.join(food)

    print(f"You are bringing {bringing}.")


if __name__ == '__main__':
    main()
