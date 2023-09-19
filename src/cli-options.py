#!/usr/bin/env python3
import argparse
import re
import sys
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=r'''
            Returns commad line flags/options parsed from the input stream.
            The options are extracted using the Python regex '(?:^\s*|.+,
            )(-{1,2}[a-zA-Z0-9\-_]+=?)', of which there can be multiple matches
            on a single line. Matches are output with the line number, a colon,
            and the flag/option itself.''')
    parser.add_argument(
        'istream',
        nargs='?',
        type=argparse.FileType('rb'),
        default=sys.stdin,
        help='''
            input file (default: read from stdin)''')
    args = parser.parse_args()
    pattern = re.compile(r'(?:^\s*|.+, )(-{1,2}[a-zA-Z0-9\-_]+=?)')
    for line_no, line in enumerate(args.istream, start=1):
        for match in pattern.finditer(line):
            print(f'{line_no}:{match.groups()[0]}')

