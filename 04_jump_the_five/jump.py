#!/usr/bin/env python3
"""Jump the Five"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(description="Jump the Five")
    parser.add_argument("str", help="Input text")

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    text = get_args().str

    transform_dict = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5"
    }

    print("".join([transform_dict.get(char, char) for char in text]))

    # encrypted_chars = []
    # for char in text:
    #     encrypted_chars.append(transform_dict.get(char, char))
    # print("".join(encrypted_chars))


if __name__ == "__main__":
    main()
