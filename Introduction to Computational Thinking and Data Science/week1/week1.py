# !/Library/Frameworks/Python.framework/Versions/2.7/bin/Python
# -*- coding: utf-8 -*-

__author__ = "Cloga Chen(Cloga0216@gmail.com)"
__copyright__ = "Copyright (c) 2014 Cloga Chen"
__createtime__ = "2014-10-26 12:43:56"
__modifytime__ = "2014-10-26 12:43:59"

PATH_TO_FILE = 'julyTemps.txt'
high = []
low = []
inFile = open(PATH_TO_FILE, 'r', 0)
for line in inFile:
    fields = line.split()
    if len(fields) != 3 or fields[0] == 'Boston' or fields[0] == 'Day':
        continue
    high.append(fields[1])
    low.append(fields[2])


def loadWords(PATH_TO_FILE):
    inFile = open(PATH_TO_FILE, 'r', 0)
    line = inFile.readline()
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    return wordlist

# loadWords(PATH_TO_FILE)

def loadWords2():
    try:
        inFile = open(PATH_TO_FILE, 'r', 0)
            #line of code to be added here#
    except IOError:
            print "The wordlist doesn't exist; using some fruits for now"
            return ['apple', 'orange', 'pear', 'lime', 'lemon', 'grape', 'pineapple']
    line = inFile.readline()
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    return wordlist