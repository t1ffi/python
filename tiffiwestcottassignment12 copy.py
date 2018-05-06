'''Tiffi Westcott

Today's assignment is solved using regular expressions to separate data and reorder it in the correct format'''

'''This imports all of the necessary items in order to complete the program below'''
import sys

import re

import time


''''Within the UAlbanyLighning.txt file, the try and except opens the file
and if it is not there it stops the program and prints the results to the user.''' 
try:
    fhand = open("UAlbanyLightning.txt")
except OSError:
    print("404 ERROR! Just kidding, but really, there isn't a file like that in sight.")
    sys.exit(0)

'''This for loop reads the text file line by line (so technically each line
is at the 0 place. Think of an excel spreadsheet.'''
for line in fhand:

    '''Tells the program to look for the numbers within the number ranges as
        listed in the parenthesis.'''
    dates = (re.findall(r'([0-9]{4})-([0-1][0-9])-([0-3][0-9])', line ))

    '''Using regular expression, this section scans the text for a predetermined
        pattern to then separate for lightning strikes.'''
    strike = (re.findall(r'([0-9]+)', line ))

    '''The double negative indicates to the program that if the line is a date
        (so excluding line one) then it will print the dates only reordered
        this time while tacking on the number of strike indicated.'''
    if (not dates) == False:
        print (dates[0][1] + " " + dates[0][2] + " " + dates[0][0] + ": " + strike[-1] + " lightning strikes were recorded on this certain date. Cool!")
