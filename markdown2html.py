#!/usr/bin/python3

"""
Script converts markdown to html:
"""
import sys
import os.path
import re
import hashlib

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)
    with open(sys.argv[1]) as read:
        with open(sys.argv[2], 'w') as html:
            for line in read:
                length = len(line)
                cheadings = line.lstrip('#')
                cheading_num = length - len(cheadings)
                if 1 <= cheading_num <= 6:
                    line = '<h{}>'.format(
                        cheading_num) + cheadings.strip() + '</h{}>\n'.format(
                        cheading_num)
                if length > 1:
                    html.write(line)
    exit (0)
