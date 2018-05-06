#Tiffi Westcott
#INF 308
#This program isolates and extracts data from the given mbox2.txt file.

#This imports time and sys to the program.
import time
import sys


#This tracks the execution time of the program.
secs = time.clock()

print ('Execution time = ', secs, 'seconds')



#Opens new or existing file from the start. 
file = open("addr.txt", "w+")



#Try and except to protect application from unopened or unopenable files.
try:
    fhand = open("mbox2.txt")
except OSError:
    print ("This file is not found")
    

#Opens mbox2.txt file and reads it to then print the email addresses collected and closes.
fhand = open('mbox2.txt')

inp = fhand.read()

print ('This file contains', len(inp), 'characters\n')

fhand.close()



#Modifies the code to extract names from document.
fhand = open('mbox2.txt')

for line in fhand:

    line = line.rstrip()    # Remove the newline character, creates blank lines

    if line.startswith('From:'):

        print (line[6:])    # Strip away ‘From:’


#Splits the information extracted to remove the @ symbol and replace it with a space by using tokens.
split = ""

fhand = open ("mbox2.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        split = split + (line[6:] + " ")

splice = split.replace("@", " ")
token = splice.split (" ")

i = 0


#Chooses every other word to be printed so only the names are printed.
#Then the file is printed and written to the addr.txt file. 
while i < len(token):
    print(token[i])
    file.write(token[i] + " ")
    i = i + 2


#Closes addr.txt file. 
file.close()



    
