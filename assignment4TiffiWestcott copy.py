# Tiffi Westcott
# Assignment #4

#Display not-so-random (corresponding) proverbs. 

import random

#Prints greeting to the user and allows a space for their input. 
print ('Welcome to the random proverb generator! Once you enter a positive integer, it will select a random proverb and print it out for you.')
userInput = input('Enter a positive integer: ')

#This insures that the input the user typed is valid and an integer.
try:
    posInput = int(userInput)
except ValueError:
    print ('That is not a valid input, please try again.')

#Echos their input.
print ('You entered ', userInput)

#Variable that finds the remainder of their input and prints the corresponding proverb with that number.
newInput = posInput%7

print ('Your random proverb is *drum roll, please*: ')

#If elif else statements that execute the above explanation!
if newInput == 0:
    print ('Absence makes the heart grow fonder.')
    print ('This means that being away from someone or something for a period of time makes you appreciate that person or thing more when you see them or it again.')

elif newInput == 1:
    print ('Actions speak louder than words.')
    print ('This means that what you do is more important than what you say.')

elif newInput == 2:
    print ('A journey of a thousand miles begins with a single step')
    print ('This means that you must begin something if you hope to finish it.')

elif newInput == 3:
    print ('All good things must come to an end.')
    print ('This means that everything ends and good times do not last forever')

elif newInput == 4:
    print ('A picture is worth a thousand words.')
    print ('This means that an image can tell a story better than words.')

elif newInput == 5:
    print ('A watched pot never boils.')
    print ('This means that if someting takes time to do, it does not help to keep constantly checking on it and to give it time.')

elif newInput == 6:
    print ('Beggars cannot be choosers')
    print ('This means that if you are in a desparate situation and on eoffers to help, you must take what you can get.')
    
