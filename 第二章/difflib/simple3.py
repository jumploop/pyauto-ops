#!/usr/bin/python
import difflib
import sys


def readfile(filename):
    try:
        fileHandle = open(filename, 'r')
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as error:
        print('Read file Error:' + str(error))
        sys.exit()


def main():
    try:
        textfile1 = sys.argv[1]
        textfile2 = sys.argv[2]
    except Exception as e:
        print("Error:" + str(e))
        print("Usage: simple3.py filename1 filename2")
        sys.exit()
    if textfile1 == "" or textfile2 == "":
        print("Usage: simple3.py filename1 filename2")
        sys.exit()
    text1_lines = readfile(textfile1)
    text2_lines = readfile(textfile2)

    d = difflib.HtmlDiff()
    print(d.make_file(text1_lines, text2_lines))


if __name__ == '__main__':
    main()
