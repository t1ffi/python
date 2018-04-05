'''
Tiffi Westcott
Assignment #9
This program takes the quote given in the assignment and changes all the words
to lower case, tokenizes the words, and uses a for loop to count and print out
all of the words. This one took me longer than usual but I got it! 
'''

str = 'Be the change that you wish to see in the world. Mahatma Gandhi'

#make a list of words strokenized from given string.

string=str.strip()
string1=string.split()

#Print string in lower in lower case and initialize count to 0.
print (string.lower())

count = 0
#Iterate over each string in the list string and iterate word count
for word in string1:
    word = word.lower()
    count += 1
    print (word)


#This prints the final word on the last line. 
print ("Word count = ",count)

