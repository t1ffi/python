#Tiffi Westcott
#Assignment 3b: this validates user input using if - else and releasing a print statement with the results accordingly.

#User inputs number
userInput = input('Enter a positive , even integer: ')

#This validates the user's input as an integer or not.
try:
    intInput = int(userInput)
except ValueError:
    print ("That's not a valid input. Try again.")

#This is the even or odd validation point.
if intInput % 2 == 0:
    print ("The input is even. Hooray!")
else:
    print ("The input is odd. Try again.")

#This is the positive or negative validation checkpoint.
if intInput > 0:
    print ("The input is positive. Hooray!")
else:
    print ("The input is negative. Try again.") 

#Final validation station! Prints the final outcome and evaluation of the input.
if intInput > 0 and intInput % 2==0:
    print ("Integer is valid: positive and even - ", intInput)

if intInput < 0 and intInput % 2 == 0:
    print ("Integer is invalid: negative and even - ", intInput)

if intInput < 0 and intInput % 2 != 0:
    print ("Integer is invalid: negative and odd - ", intInput)

if intInput > 0 and intInput % 2 != 0:
    print ("Integer is invalid: positive and odd - ", intInput)
