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
            startUnordered = False
            startOrdered = False
            paragraph = False
            for line in read:
                line = line.replace('**', '<b>', 1)
                line = line.replace('**', '</b>', 1)
                line = line.replace('__', '<em>', 1)
                line = line.replace('__', '</em>', 1)
                length = len(line)
                cheadings = line.lstrip('#')
                cheading_num = length - len(cheadings)
                cunordered = line.lstrip('-')
                cunordered_num = length - len(cunordered)
                cordered = line.lstrip('*')
                cordered_num = length - len(cordered)
                if 1 <= cheading_num <= 6:
                    line = '<h{}>'.format(
                        cheading_num) + cheadings.strip() + '</h{}>\n'.format(
                        cheading_num)
                if cunordered_num:
                    if not startUnordered:
                        html.write('<ul>\n')
                        startUnordered = True
                    line = '<li>' + cunordered.strip() + '</li>\n'
                if startUnordered and not cunordered_num:
                    html.write('</ul>\n')
                    startUnordered = False
                if cordered_num:
                    if not startOrdered:
                        html.write('<ol>\n')
                        startOrdered = True
                    line = '<li>' + cordered.strip() + '</li>\n'
                if startOrdered and not cordered_num:
                    html.write('</ol>\n')
                    startOrdered = False
                
                if not (cheading_num or startUnordered or startOrdered):
                    if not paragraph and length > 1:
                        html.write('<p>\n')
                        paragraph = True
                    elif length > 1:
                        html.write('<br/>\n')
                    elif paragraph:
                        html.write('</p>\n')
                        paragraph = False

                if length > 1:
                    html.write(line)
            if startUnordered:
                html.write('</ul>\n')
            if startOrdered:
                html.write('</ol>\n')
            if paragraph:
                html.write('</p>\n')
    exit (0)
