#!/bin/python

import argparse

parser = argparse.ArgumentParser(description='Read a file in reverse')

parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='Number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.0.1')
args = parser.parse_args()
