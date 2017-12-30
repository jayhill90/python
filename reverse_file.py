#!/bin/python

import argparse

parser = argparse.ArgumentParser(description='Read a file in reverse')

parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='Number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.0.1')
args = parser.parse_args()

try:
    f = open(args.filename)
except IOError as err:
    print("Error 404: file not found")
else:
    with open(args.filename) as f:
        limit = args.limit
        lines = f.readlines()
        lines.reverse()

        if limit:
            lines = lines[:args.limit]

        for line in lines:
            print(line.strip()[::-1])

finally:
    print("\nWe're done.")
