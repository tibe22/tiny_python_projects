#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
import sys


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        default=[sys.stdin],
                        type=argparse.FileType('rt'),
                        help='Input files(s)')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    tl, tb, tw = 0, 0, 0
    for fh in args.file:
        num_lines = 0
        num_words = 0
        num_bytes = 0
        for line in fh:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)
        tl += num_lines
        tb += num_bytes
        tw += num_words

        print(f'{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}')

    if len(args.file) > 1:
        print(f'{tl:8}{tw:8}{tb:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
