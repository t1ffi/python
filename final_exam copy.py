# Tiffi Westcott

#Final exam! :o

import os.path

#Opens the file
fname = "/Users/tiffi/Desktop/UA/Summer_17/IINF_108/Week_Four/names.txt"

#Reads the file further
with open(fname) as f:
    content = f.readlines()

#Strips whitespace
nameList = [x.strip() for x in content]

#Prints all names
print("Here is a ist of all the names from the file:")
print(nameList)

#Prints lengths
shortestName = len(nameList[0])
print 'The length of the shortest name: ', shortestName

#Prints shortest
i=0
print 'All names with the shortest lengths: '
while i < len(nameList) and len(nameList[i]) <= shortestName:
    print nameList[i]
    i += 1

#Prints number of shortest names
print 'In total, the number of names with the shortest lengths are: ', i
