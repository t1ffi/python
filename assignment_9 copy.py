# Tiffi Westcott
# Reading and Writing Files

# Oh, I see fire and I see rain!

# I used both what you announced for us to do as assignment 9 and what was written as the assignment previously in the syllabus.

fhand = open('fireice.txt')
print fhand

for line in fhand:
    print line

# Disclosure: this is what was written on the syllabus.

words = 0
fhand = open('fireice.txt')
for line in fhand:
    print line
    ln = line.split()
    words += len(ln)
    #print words
#Trying to make it clean so I am using # to only print the necessary items without repeats.
print 'The word count of this file is ', words,'.'


