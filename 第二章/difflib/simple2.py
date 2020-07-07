#!/usr/bin/python
import difflib

text1 = """text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""

text2 = """text2:
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5"""


def main():
    text1_lines = text1.splitlines()
    text2_lines = text2.splitlines()

    d = difflib.HtmlDiff()
    print(d.make_file(text1_lines, text2_lines))


if __name__ == '__main__':
    main()
