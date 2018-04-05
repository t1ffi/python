'''
Tiffi Westcott
Assignment #8
This multiline comment is very useful!
This program takes a long word and finds the vowel count after printing the first 5  letters.
'''
import time

print ("Hello! Today's long word that we will find out more about is PSEUDOPSEUDOHYPOPARATHYROIDISM")
print ("Stay tuned in to find out more about it!")
time.sleep(5)

#Assigns this word to a variable
longWord = 'PSEUDOPSEUDOHYPOPARATHYROIDISM'
#Assigns number of characters to start with and then one for each 5 vowels (not including sometimes y) ;D
letters = 0
loopA = 0
loopE = 0
loopI = 0
loopO = 0
loopU = 0
#For loop loops the program through the directions a certain amt of times until it reaches its answers.
for i in longWord:
    letters += 1
#If-elif-else statements instructs computer to pass these tests below in order to record the information.
    if i.lower() == 'a':
        loopA += 1
    elif i.lower() == 'e':
        loopE += 1
    elif i.lower() == 'i':
        loopI += 1
    elif i.lower() == 'o':
        loopO += 1
    elif i.lower() == 'u':
        loopU += 1
    else:
        pass
'''
Print statements that tell the user what the program found including the first 5
letters of the word and the amount of each vowel that was in the word. 
'''
print ("Dun dun dun dah! Here are the results:")
print ('The number of letters in the long word is ', letters)
print ("")
print ("The number of times 'a' is in the long word is ", loopA)
print ("The number of times 'a' is in the long word is ", loopE)
print ("The number of times 'a' is in the long word is ", loopI)
print ("The number of times 'a' is in the long word is ", loopO)
print ("The number of times 'a' is in the long word is ", loopU)
print ("")
print (longWord[:5], "are the first 5 letters of the word! Thanks for your inquiry.")
