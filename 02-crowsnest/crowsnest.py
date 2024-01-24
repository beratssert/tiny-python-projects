#!/usr/bin/env python3
"""Crow's Nest -- choose the correct article"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article")
    parser.add_argument('word', help='A word')

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    word = get_args().word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'

    print(f"Ahoy, Captain, {article} {word} off the larboard bow!")


if __name__ == "__main__":
    main()
