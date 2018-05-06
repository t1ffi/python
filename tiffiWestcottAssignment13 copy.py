'''Tiffi Westcott
This program opens a text file (in this case A Tale of Two Cities 
by Charles Dickens but it can work for any text file), 
scans it through the program, and winds the unique word count to 
spit out to the user'''


import string
import sys


# Looks for tale4653.txt
try:
    fhand = open("tale4653.txt")
except OSError:
    print("Whoops! This file was not found. Please try again.")
    sys.exit(0)

#Puts word count in variable
wordcount = dict()

#For loop that splits, lowercases, and takes out string puncuation from text
for line in fhand:
    line = line.translate(None, string.punctuation)
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

#Closes document that was previously opened
fhand.close()

#Finishes the sort to print the list out to the user.
wordlist = wordcount.keys()
wordlist.sort()
for key in wordlist:
    print (key, wordcount[key])
