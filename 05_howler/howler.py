#!/usr/bin/env python3
"""Howler (upper-cases input)"""

import argparse
import os
import io
import sys


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(description="Howler (upper-cases input)")
    parser.add_argument("text",
                        metavar="text",
                        type=str,
                        help="Input string or file")
    parser.add_argument("-o",
                        "--outfile",
                        metavar="str",
                        type=str,
                        default="",
                        help="Output filename")
    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text, "rt")
    else:
        args.text = io.StringIO(args.text + "\n")

    return args


def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = open(args.outfile, "wt") if args.outfile else sys.stdout
    for line in args.text:
        out_fh.write(line.upper())
    out_fh.close()
    args.text.close()


if __name__ == "__main__":
    main()
