#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2022-06-06
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='picnic nargs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        nargs='+',
                        type=str,
                        help='A positional argument')


    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg = args.positional
    '''
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on

    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg = "{flag_arg}"')
    print(f'positional = "{pos_arg}"')
    '''

    length = len(pos_arg)
    temp_str = ''
    if args.sorted:
        pos_arg.sort()
    if length == 1:
        temp_str = pos_arg[0]
    elif length == 2:
        temp_str = ' and '.join(pos_arg)
    elif length > 2:
        pos_arg[-1] = 'and ' + pos_arg[-1]
        temp_str = ', '.join(pos_arg)

    print(f'You are bringing {temp_str}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
