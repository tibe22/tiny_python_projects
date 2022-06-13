#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
from pprint import pprint as pp


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+',
                        type=str,
                        help='Letter(s)')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # lookup = {}
    # for line in args.file:
    #     lookup[line[0].upper()] = line.rstrip()
    '''dict. comprehension'''
    lookup = { line[0].upper(): line.rstrip() for line in args.file }

    # pp(lookup)


    for letter in args.letter:
        # if letter.upper() in lookup:
        #     print(lookup[letter.upper()])
        # else:
        #     print(f'I do not know "{letter}".')
        print(lookup.get(letter.upper(),f'I do not know "{letter}".'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
