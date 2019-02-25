#!/usr/bin/python

"""Flag misspellings"""

import re
import string
import sys

words = []
input = []

# Load English
with open("english-words/words.txt") as wordfile:
        dirtywords = wordfile.readlines()

for word in dirtywords:
        words.append(word.strip().lower())
        
# Load a little specialist language

for word in ('ghe', 'github', 'nuget', 'oauth', 'pkix', 'ssl', 'http', 'https', 'ssh', 'netrc'):
        words.append(word.strip().lower())

with open(sys.argv[1]) as source:
        inputlines = source.readlines()

for line in inputlines:
        line = line.lower().replace('-', ' ') #.translate(None, string.punctuation)
        line = line.lower().replace('/', ' ') #.translate(None, string.punctuation)
        line = line.lower().replace('*', ' ')
        line = line.lower().replace('#', ' ')
        line = line.lower().replace('(', ' ')
        line = line.lower().replace(')', ' ')
        
        line = line.translate(None, string.punctuation)
        
        for word in line.split():
                if word not in words and re.search("[a-z]", word):
                        #print(line)
                        msg = 'Could not find "' + word + '" in dict'
                        print(msg)
